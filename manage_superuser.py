import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ll_project.settings")
django.setup()  # ← 這行會初始化 Django 環境


from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv("SUPERUSER_NAME")
email = os.getenv("SUPERUSER_EMAIL")
password = os.getenv("SUPERUSER_PASSWORD")

if not all([username, email, password]):
    print("❌ Missing environment variables for superuser.")
else:
    if not User.objects.filter(username=username).exists():
        User.objects.create_superuser(username=username, email=email, password=password)
        print(f"✅ Superuser '{username}' created successfully!")
    else:
        print(f"ℹ️ Superuser '{username}' already exists.")
