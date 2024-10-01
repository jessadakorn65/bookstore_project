from django.shortcuts import render, redirect, get_object_or_404
from .models import Book
from .forms import BookForm, UserRegisterForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

class ChangePasswordView(PasswordChangeView):
    form_class = PasswordChangeForm
    success_url = reverse_lazy('home')
    template_name = 'store/change_password.html'

# แสดงรายการหนังสือทั้งหมด พร้อมการค้นหา
def book_list(request):
    query = request.GET.get('q')  # รับค่าจากคีย์เวิร์ดที่ผู้ใช้ค้นหา
    if query:
        books = Book.objects.filter(title__icontains=query)  # ค้นหาชื่อหนังสือที่ตรงกับคีย์เวิร์ด
    else:
        books = Book.objects.all()  # ถ้าไม่มีคีย์เวิร์ดให้แสดงหนังสือทั้งหมด
    return render(request, 'store/book_list.html', {'books': books, 'query': query})

# แสดงรายละเอียดหนังสือ
def book_detail(request, id):
    book = get_object_or_404(Book, id=id)
    return render(request, 'store/book_detail.html', {'book': book})

# เพิ่มหนังสือใหม่
@login_required
def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book added successfully!')
            return redirect('store:book_list')
    else:
        form = BookForm()
    return render(request, 'store/book_form.html', {'form': form})

# แก้ไขข้อมูลหนังสือ
@login_required
def book_update(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            messages.success(request, 'Book updated successfully!')
            return redirect('store:book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'store/book_form.html', {'form': form})

# ลบหนังสือ
@login_required
def book_delete(request, id):
    book = get_object_or_404(Book, id=id)
    if request.method == 'POST':
        book.delete()
        messages.success(request, 'Book deleted successfully!')
        return redirect('store:book_list')
    return render(request, 'store/book_delete.html', {'book': book})

# ลงทะเบียนผู้ใช้ใหม่
def user_register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, 'Registration successful! Please login.')
            return redirect('store:registration_success')
    else:
        form = UserRegisterForm()
    return render(request, 'store/register.html', {'form': form})

# เข้าสู่ระบบผู้ใช้
def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'You have successfully logged in.')
            return redirect('store:book_list')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'store/login.html')

# ออกจากระบบผู้ใช้
@login_required
def user_logout(request):
    logout(request)
    messages.info(request, 'You have successfully logged out.')
    return redirect('store:login')

# แสดงข้อความเมื่อการลงทะเบียนสำเร็จ
def registration_success(request):
    return render(request, 'store/registration_success.html')

def home(request):
    return render(request, 'store/home.html')  # ปรับเปลี่ยนเป็นชื่อไฟล์ที่คุณใช้สำหรับหน้า Home
