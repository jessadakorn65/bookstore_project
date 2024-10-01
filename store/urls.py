from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home, name='home'),  # หน้าแรกของเว็บไซต์
    path('create/', views.book_create, name='book_create'),  # สร้างหนังสือใหม่
    path('update/<int:id>/', views.book_update, name='book_update'),  # แก้ไขหนังสือ
    path('delete/<int:id>/', views.book_delete, name='book_delete'),  # ลบหนังสือ
    path('detail/<int:id>/', views.book_detail, name='book_detail'),  # ดูรายละเอียดหนังสือ

    path('register/', views.user_register, name='register'),  # ลงทะเบียนผู้ใช้
    path('login/', views.user_login, name='login'),  # เข้าสู่ระบบ
    path('logout/', views.user_logout, name='logout'),  # ออกจากระบบ
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),  # เปลี่ยนรหัสผ่าน
    path('registration_success/', views.registration_success, name='registration_success'),  # หน้าสำเร็จการลงทะเบียน

    # URL สำหรับการจัดการรีเซ็ตรหัสผ่าน (Django Auth)
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='store/password_reset.html'), name='password_reset'),  # รีเซ็ตรหัสผ่าน
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='store/password_reset_done.html'), name='password_reset_done'),  # ข้อความยืนยันการรีเซ็ตรหัสผ่าน
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='store/password_reset_confirm.html'), name='password_reset_confirm'),  # ยืนยันการรีเซ็ตรหัสผ่าน
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='store/password_reset_complete.html'), name='password_reset_complete'),  # หน้าสำเร็จการรีเซ็ตรหัสผ่าน

    # เส้นทางสำหรับรายการหนังสือ
    path('books/', views.book_list, name='book_list'),  # แสดงรายการหนังสือ
]
