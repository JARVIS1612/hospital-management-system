from django.shortcuts import render

# Create your views here.

Facilities = [
    {
        'f': 'Brain Strock Prevention Clinic',
        'fd': '''Stroke prevention clinic looks into assessment of risk factors
                which can lead to a stroke. We suggest lifestyle changes &
                adapting healthy habits.'''
    },
    {
        'f': 'Heart Rhythm Clinic',
        'fd': '''Consults for the improper heart-beat, whether irregular, too
                fast or too slow.'''
    },
    {
        'f': 'Skin & Hair Clinic',
        'fd': '''A clinic that specialize in treating skin & hair to ensure you
                keep looking awesome.'''
    },
    {
        'f': 'Allergy Clinic',
        'fd': '''Latest technologies can detect around 300 Allergens from a
                single serum sample. Allergy clinic helps in diagnosing specific
                agents or triggers for which a person is allergic to.'''
    },
    {
        'f': 'Heart Failure Clinic',
        'fd': '''A heart failure occurs when heart muscles doesn’t pump blood in
                the way it should; thus blood often backs up and causes fluid to
                build up in Lungs and Legs, this build-up fluid can cause
                shortness of breath.'''
    },
    {
        'f': 'Sleep Disorder Clinic',
        'fd': '''Sleep Disorder Clinic tests and monitor Sleep Apnea. The test
                includes monitoring Heart, Lung and Brain activity, breathing
                patterns, arm & leg movements, and blood oxygen levels when you
                are fast asleep.'''
    }
]


def home(request):
    context = {'Facilities': Facilities}
    return render(request, 'home/home.html', context)


def about(request):
    context = {'title': 'About'}
    return render(request, 'home/about.html', context)
