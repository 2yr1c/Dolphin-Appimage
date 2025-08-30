import os

def split_file(file_path, chunk_size=20*1024*1024):
    """
    把大文件分割成多个小文件，每个 chunk_size 字节（默认20MB）
    """
    file_size = os.path.getsize(file_path)
    file_name = os.path.basename(file_path)
    base_name, ext = os.path.splitext(file_name)

    with open(file_path, "rb") as f:
        part_num = 1
        while True:
            chunk = f.read(chunk_size)
            if not chunk:
                break
            part_filename = f"{base_name}_part{part_num}{ext}"
            with open(part_filename, "wb") as part_file:
                part_file.write(chunk)
            print(f"生成: {part_filename} ({len(chunk)} bytes)")
            part_num += 1

    print(f"完成！共分成 {part_num-1} 个小文件。")

if __name__ == "__main__":
    # 使用示例
    split_file("Dolphin-23.08.1-x86-64.AppImage")
