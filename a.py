import os
import glob
import subprocess

def get_mp4_ts(ts_path, mp4_path):
    # 检查输入路径
    if not os.path.exists(ts_path):
        print(f"Error: Input path '{ts_path}' does not exist.")
        return

    # 创建目标目录
    os.makedirs(mp4_path, exist_ok=True)

    # 获取 .ts 文件列表
    ts_list = glob.glob(os.path.join(ts_path, "*.ts")) if os.path.isdir(ts_path) else [ts_path]
    if not ts_list:
        print("No .ts files found.")
        return

    # 指定 FFmpeg 路径（可选，确保 FFmpeg 可用）
    ffmpeg_exe = "ffmpeg"  # 或 r"C:\path\to\ffmpeg\bin\ffmpeg.exe"

    # 转换文件
    for index, ts_file in enumerate(ts_list):
        mp4_file = os.path.join(mp4_path, os.path.basename(ts_file).replace(".ts", ".mp4"))
        try:
            subprocess.run(
                [ffmpeg_exe, '-i', ts_file, '-c:v', 'copy', '-c:a', 'copy', mp4_file],
                check=True,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )
            print(f"Converted: {ts_file} -> {mp4_file} ({index + 1}/{len(ts_list)})")
        except FileNotFoundError:
            print("Error: FFmpeg not found. Ensure it is installed and added to PATH.")
            break
        except subprocess.CalledProcessError as e:
            print(f"Error converting {ts_file}: {e.stderr.decode()}")

if __name__ == '__main__':
    ts_path = r"D:\Edge\下载"  # 输入目录或单个文件路径
    mp4_path = r"D:\video"    # 输出目录
    get_mp4_ts(ts_path, mp4_path)
