from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'index.html')

def summarizer(request):
    roviq_categories = ["Engine Control Room", "Compressor Room", "Interview - Security Officer", "Main Deck", "Interview Senior Officer", "Steering Gear", "Interview - Deck Rating", "Interview - Electrician / ETO", "Mooring Decks", "Interview - Engineer Officer", "Interview - Rating", "Interview - Deck Officer", "Cargo Control Room", "Bow Loading Area", "Chief Engineer's Office", "Lifeboat deck", "Engine Room", "Bridge", "Forecastle", "Emergency Headquarters.", "Internal Accommodation", "Interview - Galley Rating", "Documentation", "Pre-board", "Exterior Decks", "Approaching Vessel", "Interview - Engine Rating", "Cargo Manifold", "Pumproom", "Anywhere", "Aft Mooring Deck"]

    context = {"var1":roviq_categories}
    return render(request, 'summarizer.html', context)

def uploads(request):
    return render(request, 'uploads.html')

def inspection(request):
    return render(request, 'inspection.html')