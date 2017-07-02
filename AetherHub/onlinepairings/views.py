from django.shortcuts import render, get_object_or_404, redirect
from AetherHub.onlinepairings.models import Event
from AetherHub.onlinepairings.models import Player
from AetherHub.onlinepairings.forms import DocumentForm, PlayerLookupForm, ControlForm
from AetherHub import WER_parser
from AetherHub import settings

# Create your views here.
def event_list(request):
    myevents = Event.objects.all()
    context = {'myevents':myevents,}
    return render(request, 'onlinepairings/event_list.html', context)

def event_details(request, pk):
    myevents = get_object_or_404(Event, pk=pk)
    allplayers = Player.objects.filter(eventID = pk)
    #context = {'myevents':myevents, 'form':form, 'lookup_form':lookup_form, 'allplayers':allplayers, 'lookup_result':lookup_result}
    lookup_resultP = '0'
    lookup_resultT = '0'
    lookup_form = PlayerLookupForm(prefix='lookup_form')
    form = DocumentForm(prefix='form')
    control_form = ControlForm(prefix='control_form')

    if request.method == 'POST':
        action = request.POST['action']

        if "form1" in request.POST:
            form = DocumentForm(request.POST, request.FILES, prefix ='form')
            if form.is_valid():
                init_obj = form.save(commit=False)
                init_obj.save()
                a = Event.objects.get(pk=pk)
                a.WER_path = init_obj.document.url
                a.Current_round = init_obj.current_round
                a.save()
                form.save()
                if myevents.WER_path != '0':
                    WER_parser.getXML(settings.BASE_DIR + myevents.WER_path)
                    WER_parser.loadplayers(pk)
                return redirect('event_details',pk)

        if "form2" in request.POST:
            lookup_form = PlayerLookupForm(request.POST, prefix = 'lookup_form')
            if lookup_form.is_valid():
                init_obj = lookup_form.save(commit=False)
                if init_obj.DCI_lookup:
                    a = init_obj.DCI_lookup
                    lookup_resultP = WER_parser.findme(a, pk)
                if init_obj.Table_lookup:
                    a = init_obj.Table_lookup
                    lookup_resultT = WER_parser.findtables(a, pk) 
        
        if "formC" in request.POST:       
                control_form = ControlForm(request.POST, prefix = 'control_form')
                if control_form.is_valid():
                    init_obj = control_form.save(commit = False)
                    a = init_obj.roundUpdate
                if myevents.WER_path != '0':
                    WER_parser.getXML(settings.BASE_DIR + myevents.WER_path)
                    WER_parser.loadround(pk,a)

    return render(request, 'onlinepairings/event_details.html', {
        'lookup_form':lookup_form,
        'form':form,
        'control_form':control_form,
        'myevents':myevents,
        'allplayers':allplayers,
        'lookup_resultT':lookup_resultT,
        'lookup_resultP':lookup_resultP,
    })
    

def WER_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('event_list')
    else:
        form = DocumentForm()
    return render(request, 'onlinepairings/WER_upload.html', {
        'form': form
    })