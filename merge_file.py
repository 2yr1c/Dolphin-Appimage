import os
import re


def merge_files(output_file, parts_dir="."):
    """
    合并分割的小文件为一个大文件
    自动识别 *_partN.* 格式
    """
    # 找到所有分片文件
    files = [f for f in os.listdir(parts_dir) if re.search(r"_part\d+\.", f)]

    if not files:
        print("没有找到分片文件！")
        return

    # 按 part 序号排序
    files.sort(key=lambda x: int(re.search(r"_part(\d+)", x).group(1)))

    with open(output_file, "wb") as outfile:
        for f in files:
            part_path = os.path.join(parts_dir, f)
            with open(part_path, "rb") as infile:
                data = infile.read()
                outfile.write(data)
            print(f"合并: {f} ({len(data)} bytes)")

    print(f"完成！合并生成 {output_file}")


if __name__ == "__main__":
    # 使用示例：手动指定输出文件名
    merge_files("Dolphin-23.08.1-x86-64_merged.AppImage")
