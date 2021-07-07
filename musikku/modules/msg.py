import os
from musikku.config import SOURCE_CODE,ASSISTANT_NAME,PROJECT_NAME,SUPPORT_GROUP,UPDATES_CHANNEL
class Messages():
      START_MSG = "**MERHABA👋 [{}](tg://user?id={})!**\n\n🤖 Telegram gruplarında sesli sohbette müzik çalmak için oluşturulmuş bir müzik botuyum.\n\n✅ Komut /help Kullanım Rehberidir Lütfen Bakın"
      HELP_MSG = [
        ".",
f"""
**Merhaba 👋 Hoş Geldiniz {PROJECT_NAME}

⚡ {PROJECT_NAME} Grup sesli sohbetinizde ve Kanal sesli sohbetinizde müzik çalabilir ASİSTAN GRUPTA OLMADAN ÇALIŞMAZ !!

⚡ Botun Yardımcı Asistanı >> @{ASSISTANT_NAME}**
""",

f"""
📌 **Gruplarda Botu Kullanma Rehberi**

1) Bu botu Grubunuza ekleyin
2) Bu Botu Ve Asitanı @{ASSISTANT_NAME} yönetici olarak ve sesli sohbet yetkisi verin.
2) Sesli Sohbet veya Grup Sesli Sohbet'i açın
3) Ardından /oynat [Şarkı Adı] Yazın.
*)Çalışırsa kullanılabilir demektir, bir hata varsa Gruba @{ASSISTANT_NAME} eklemeyi deneyin ve yukarıdaki yöntemi tekrarlayın.

**Grupta Bot Kullanan Komutların Listesi**

⎋ **İşte birkaç seçenek 🎧**

- /oynat şarkı adı: şarkı adını yazarak bir şarkı çalın yanıtlanan Müziği Oynatmaz.

⎋ **Diğer Komutların Listesi**

- /atla : Diğer Şarkıya Atlar
- /duraklat : Oynatılan Şarkıyı Duraklatır.
- /devam : Şarkıyı çalmaya devam ettirir.
- /bitir : Müzik çalmayı durdurur.
- /vcbak :  Seste çalan şarkıyı gösterir.
- /playlist : Çalma Listesini Gösterir.

""",
        
f"""
⎋ ** Diğer Komutların Listesi**

- /reload : yönetici listesini güncelle
: Grubunuza Asistanı Eklemeyi Unutmayın @{ASSISTANT_NAME} Gerçek Asistandır.

""",

f"""
**🦞 @NetdBots EMEĞİ GEÇEN HERKESE TEŞEKKÜRLER. 🦞** 
"""
      ]
