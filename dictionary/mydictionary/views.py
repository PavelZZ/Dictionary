import os
from django.shortcuts import render, redirect
from django.conf import settings

FILE_PATH = os.path.join(settings.BASE_DIR, "file.txt")

def add_to_file(word1: str, word2: str):
    with open(FILE_PATH, "a", encoding="utf-8") as file:
        file.write(word1 + "-" + word2 + "\n")

def read_from_file():
    if not os.path.exists(FILE_PATH):
        return [], []
    with open(FILE_PATH, "r", encoding="utf-8") as file:
        lines = file.read().splitlines()
    words1 = []
    words2 = []
    for line in lines:
        if "-" in line:
            w1, w2 = line.split("-", 1)
            words1.append(w1)
            words2.append(w2)
    return words1, words2

def home(request):
    return render(request, "mydictionary/home.html")

def words_list(request):
    words1, words2 = read_from_file()
    words = list(zip(words1, words2))
    context = {
        "words": words,
    }
    return render(request, "mydictionary/words_list.html", context)

def add_word(request):
    if request.method == "POST":
        word1 = request.POST.get("word1")
        word2 = request.POST.get("word2")
        if word1 and word2:
            add_to_file(word1, word2)
        # После добавления перенаправляем пользователя на домашнюю страницу
        return redirect("home")
    return render(request, "mydictionary/add_word.html")
