import yt_dlp

def download_youtube_mp3(video_url):
    # Pengaturan untuk mengonversi video menjadi MP3 kualitas tinggi
    ydl_opts = {
        'format': 'bestaudio/best',  # Mengambil kualitas audio terbaik
        'ffmpeg_location': '.',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio', # Menggunakan FFmpeg untuk ekstrak audio
            'preferredcodec': 'mp3',     # Format akhir
            'preferredquality': '320',   # Kualitas audio maksimal 320kbps
        }],
        'outtmpl': '%(title)s.%(ext)s',  # Menamai file sesuai judul asli YouTube
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        print("Sedang memproses dan mengonversi... Mohon tunggu 🔥")
        ydl.download([video_url])
        print("Selesai! Lagu kamu sudah siap 🎧")

# Uji coba kodinganmu di sini
url_input = input("Masukkan link YouTube: ")
download_youtube_mp3(url_input)
