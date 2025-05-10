# Plik do definiowania widoków, które są renderowane za pomocą szablonizatora Jinja oraz wyświetlane w przeglądarce

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages #to show message back for errors
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

@login_required
def skills(request):
    values = {
        'skills': [
            {
                'skill': 'Logic',
                'attribute': 'Intellect',
                'description': 'Logic urges you to analyze the living daylights out of the case. It enables you to piece evidence together, detect inconsistencies in statements, and impress everyone with your astonishing conclusions.',
                'skill_image': 'Portrait_logic.png',
            },
            {
                'skill': 'Encyclopedia',
                'attribute': 'Intellect',
                'description': 'Encyclopedia makes you a know-it-all, turning your mind into a database of facts. It enables you to draw on these facts innately, offering a wealth of background knowledge to all things related and unrelated to your case.',
                'skill_image': 'Portrait_encyclopedia.png',
            },
            {
                'skill': 'Rhetoric',
                'attribute': 'Intellect',
                'description': 'Rhetoric urges you to debate, make intellectual discourse, nitpick – and win. It enables you to break down arguments and hear what people are really saying.',
                'skill_image': 'Portrait_rhetoric.png',
            },
            {
                'skill': 'Drama',
                'attribute': 'Intellect',
                'description': 'Drama urges you to treat the world as a stage – and on it, to perform. It will enable you to lie, to concoct the most elaborate and wonderful stories.',
                'skill_image': 'Portrait_drama.png',
            },
            {
                'skill': 'Conceptualization',
                'attribute': 'Intellect',
                'description': 'Conceptualization has a special role it wants you to play in this world – not the role of cop, but of Art Cop. It enables you to make fresh associations, to delve into world-concepts from Jan Kaarp’s postmodernist karperie, to Revachol’s arabesque architectural style dideridada.',
                'skill_image': 'Portrait_conceptualization.png',
            },
            {
                'skill': 'Visual Calculus',
                'attribute': 'Intellect',
                'description': 'Visual Calculus verses you not only in the laws of the state, but the laws of nature. It enables you to create virtual crime-scene models in your mind’s eye.',
                'skill_image': 'Portrait_visual_calculus.png',
            },
            {
                'skill': 'Volition',
                'attribute': 'Psyche',
                'description': 'Volition urges you to be a good guy – to others and to yourself. It enables you to resist temptation: be it in a bottle, between a pair of legs, or at the end of an iron barrel which promises oblivion.',
                'skill_image': 'Portrait_volition.png',
            },
            {
                'skill': 'Inland Empire',
                'attribute': 'Psyche',
                'description': 'Inland Empire is the unfiltered wellspring of imagination, emotion, and foreboding. It enables you to grope your way through invisible dimensions of reality, gaining insight into that which sight can’t see.',
                'skill_image': 'Portrait_inland_empire.png',
            },
            {
                'skill': 'Empathy',
                'attribute': 'Psyche',
                'description': 'Empathy breaks into the souls of others and forces you to feel what’s inside. It enables you to notice social cues others may miss.',
                'skill_image': 'Portrait_empathy.png',
            },
            {
                'skill': 'Authority',
                'attribute': 'Psyche',
                'description': 'Authority urges you to assert and reassert your dominance over those around you. It enables you to understand the power dynamics of groups of thugs, know how far you can push a perpetrator, and how to establish control of situations.',
                'skill_image': 'Portrait_authority.png',
            },
            {
                'skill': 'Espirit de Corps',
                'attribute': 'Psyche',
                'description': 'Esprit de Corps is the very spirit of policing: the cop-geist. It enables you to understand your blue-souled sisters and brothers.',
                'skill_image': 'Portrait_espirit_de_corps.png',
            },
            {
                'skill': 'Suggestion',
                'attribute': 'Psyche',
                'description': 'Suggestion urges a soft-power approach. If people think they want what you want, you’ve already won. This skill enables you to implant ideas into the minds of others.',
                'skill_image': 'Portrait_suggestion.png',
            },
            {
                'skill': 'Endurance',
                'attribute': 'Physique',
                'description': 'Endurance is your metabolism and circulatory system. It improves your Health – one of the two health pools in the game. It enables to survive being a cop.',
                'skill_image': 'Portrait_endurance.png',
            },
            {
                'skill': 'Pain Threshold',
                'attribute': 'Physique',
                'description': 'Pain Threshold ignores damage so you can push on, bloodied and crawling, to the bitterest end. It enables you to negate damage you would otherwise take.',
                'skill_image': 'Portrait_pain_threshold.png',
            },
            {
                'skill': 'Physical Instrument',
                'attribute': 'Physique',
                'description': 'Physical Instrument is not only your muscles and your skeleton – it is your ability to use them effectively.',
                'skill_image': 'Portrait_physical_instrument.png',
            },
            {
                'skill': 'Electrochemistry',
                'attribute': 'Physique',
                'description': 'Electrochemistry is the animal within you, the beast longing to be unleashed to indulge and enjoy. It enables you to take drugs with fewer negative side-effects.',
                'skill_image': 'Portrait_electrochemistry.png',
            },
            {
                'skill': 'Shivers',
                'attribute': 'Physique',
                'description': 'Shivers come when the temperature drops and you become more keenly aware of your surroundings. It enables you to hear the city itself, to truly belong to the streets.',
                'skill_image': 'Portrait_shivers.png',
            },
            {
                'skill': 'Half Light',
                'attribute': 'Physique',
                'description': 'Half Light is your fight-or-flight response. It enables you to sense the way situations are about to turn. It injects palpable fear into your heart – fear that urges you act before it’s too late.',
                'skill_image': 'Portrait_half_light.png',
            },
            {
                'skill': 'Hand/Eye Coordination',
                'attribute': 'Motorics',
                'description': 'Hand/Eye Coordination loves the interaction between you and things that fly in the air. It enables you to catch coins from mob bosses, shoot straight, and understand firearms intimately.',
                'skill_image': 'Portrait_hand_eye_coordination.png',
            },
            {
                'skill': 'Perception',
                'attribute': 'Motorics',
                'description': 'Perception wants you to be open to the world – with eyes, ears, and nose working at full capacity. It enables you to take in what others don’t notice.',
                'skill_image': 'Portrait_perception.png',
            },
            {
                'skill': 'Reaction Speed',
                'attribute': 'Motorics',
                'description': 'Reaction Speed is the agility of your body and mind. It is instinct. It enables you to dodge punches, knives, bullets. Also suckers punches of the verbal kind.',
                'skill_image': 'Portrait_reaction_speed.png',
            },
            {
                'skill': 'Savoir Faire',
                'attribute': 'Motorics',
                'description': 'Savoir Faire urges you to be better than you are: it urges you to be disco. Slip by others in Samaran boxing style, then tumble out the back with unexpected acrobatics.',
                'skill_image': 'Portrait_savoir_faire.png',
            },
            {
                'skill': 'Interfacing',
                'attribute': 'Motorics',
                'description': 'Interfacing wants you to connect to machines: to use and improve them, because that makes you a better human organism.',
                'skill_image': 'Portrait_interfacing.png',
            },
            {
                'skill': 'Composure',
                'attribute': 'Motorics',
                'description': 'Composure wants you to not crack: or, at least, it wants you to not crack in front of other people. It enables you to put up a strong front.',
                'skill_image': 'Portrait_composure.png',
            },
            
        ]
    }

    return render(request, 'main/skills.html', values)

def about(request):
    return render(request, 'main/about.html')

# Using the Django authentication system (Django Documentation)
# https://docs.djangoproject.com/en/5.1/topics/auth/default/
def login_user(request):
    if request.user.is_authenticated:
        return redirect('home')
     
    if request.method == 'POST':
         user = authenticate(username=request.POST['username'], password=request.POST['password'])
         if user is not None:
             login(request, user)
             if request.session.get('next'):
                return redirect(request.session.pop('next'))
             
             return redirect('home')
         else:
             messages.error(request, 'Invalid credentials')
             return redirect('login_user')
         
    if request.GET.get('next'):
        request.session['next'] = request.GET['next']

    return render(request, 'main/users/login.html')

def register(request):
    if request.user.is_authenticated:
         return redirect('home')
    
    if request.method == 'POST':
        user = User.objects.create_user(request.POST['username'], request.POST['email'], request.POST['password'])
        login(request, user)
        return redirect('home')
    
    return render(request, 'main/users/register.html')

def logout_user(request):
    logout(request)
     
    return redirect('home')