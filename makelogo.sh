ffmpeg -loop 1 -i data/logo.png -c:v libx264 -t 5 -pix_fmt yuv420p -vf data/logo.mp4
