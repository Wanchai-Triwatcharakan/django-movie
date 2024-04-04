from django.shortcuts import render
from django.http import HttpResponse
from .models import Data_movie
from .models import Data_list
from .models import Category
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.
def index(request):
    data_movie = Data_movie.objects.all() # ดึงข้อมูลทั้งหมด
    
    # Paginator
    paginator = Paginator(data_movie[::-1],16) #Paginator(ตัวแปรที่ต้องการ,การแสดงผลต่อ 1 หน้า) [start:stop:step-1] ย้อนกลับ
    try:
        page =int(request.GET.get('page','1')) # ตัวแปร pageในวงเล็บ(จะดึงค่าพารามิเตอร์ 'page' จาก URL ) มีค่าเป็น 1
    except:
        page = 1 # ถ้าตัวแปร page ยังไม่ได้มีการนิยามค่า ให้ page มีค่า = 1
        
    try:
        movie_page = paginator.page(page) # ให้ค่าใน paginator อ้างอิงตามตัวแปร page
    except(EmptyPage,InvalidPage):
        movie_page = paginator.page(paginator.num_pages) # กำหนดให้ paginator เป็นหน้าล่าสุด โดย paginator.num_pages จะคืนค่าเป็นจำนวนหน้าทั้งหมดใน Paginator
        
    return render(request, "index.html",{'data_movie':movie_page})

def play(request, play_id):
    myPlay = True
    play_movie = Data_movie.objects.get(id=play_id) # ดึงข้อมูลตาม id id ชื่อฟิลด์ id ในฐานข้อมูล play_id คือ id ที่ถูกส่งมา
    return render(request, "play.html",{"play_movie":play_movie, 'myPlay':myPlay})

def list(request, play_id):
    play_movie = Data_movie.objects.get(id=play_id)
    list_movie = Data_list.objects.filter(main_id=play_id) # ดึงข้อมูลที่มี main_id เหมือนกัน
    return render(request, "list.html",{"list_movie":list_movie,"play_movie":play_movie})

def play_list(request, play_id, part_id):
    play_movie = Data_movie.objects.get(id=play_id)
    list_movie = Data_list.objects.get(part=part_id)
    part = Data_list.objects.filter(main_id=play_id)
    return render(request, 'play.html', {'play_movie':play_movie, 'list_movie':list_movie, 'part':len(part)}) # len() หรือ .count() ใช้หาจำนวนข้อมูลใน QuerySet

def search (request):
    searching = request.GET.get('searching')
    results = Data_movie.objects.filter(name__icontains=searching) # name__icontains=searching คือ การค้นหาข้อมูลในฟิลด์ name ของโมเดล โดยตรวจสอบว่าค่าในฟิลด์ name มีคำที่ประกอบด้วยคำที่ระบุในตัวแปร searching หรือไม่
    return render(request, 'search.html' , {'results':results , 'searching':searching})

def thai_movie_category (request):
    name_category = Category.objects.get(name_category="หนังไทย")
    thai_movies = Data_movie.objects.filter(category=name_category)
    print (Category.name_category)
    paginator = Paginator(thai_movies[::-1],16)
    try:
        page =int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        movie_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        movie_page = paginator.page(paginator.num_pages)
    
    return render(request, 'category.html' , {'data_movie':movie_page , 'name_category':name_category})

def eng_movie_category (request):
    name_category = Category.objects.get(name_category="หนังฝรั่ง")
    eng_movies = Data_movie.objects.filter(category=name_category)
    
    paginator = Paginator(eng_movies[::-1],16)
    try:
        page =int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        movie_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        movie_page = paginator.page(paginator.num_pages)
    
    return render(request, 'category.html' , {'data_movie':movie_page , 'name_category':name_category})

def korea_series_category (request):
    name_category = Category.objects.get(name_category="ซีรีย์เกาหลี")
    korea_series = Data_movie.objects.filter(category=name_category)
    paginator = Paginator(korea_series[::-1],16)
    try:
        page =int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        movie_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        movie_page = paginator.page(paginator.num_pages)
    
    return render(request, 'category.html' , {'data_movie':movie_page , 'name_category':name_category})

def eng_series_category (request):
    name_category = Category.objects.get(name_category="ซีรีย์ฝรั่ง")
    eng_series = Data_movie.objects.filter(category=name_category)
    paginator = Paginator(eng_series[::-1],16)
    try:
        page =int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        movie_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        movie_page = paginator.page(paginator.num_pages)
    
    return render(request, 'category.html' , {'data_movie':movie_page , 'name_category':name_category})

def cartoon_category (request):
    name_category = Category.objects.get(name_category="การ์ตูน")
    cartoons = Data_movie.objects.filter(category=name_category)
    paginator = Paginator(cartoons[::-1],16)
    try:
        page =int(request.GET.get('page','1'))
    except:
        page = 1

    try:
        movie_page = paginator.page(page)
    except(EmptyPage,InvalidPage):
        movie_page = paginator.page(paginator.num_pages)
    
    return render(request, 'category.html' , {'data_movie':movie_page , 'name_category':name_category})