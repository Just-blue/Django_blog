# 删除没有使用到的图片
import django
from django.conf import settings
import os
import fnmatch
from blog_project.settings import BASE_DIR


def load_setting():
    os.environ['DJANGO_SETTINGS_MODULE'] = 'blog_project.settings'
    django.setup()

    # 设置为False，避免出现模型查询输出SQL语句
    settings.DEBUG = False


def main():
    # 加载django配置
    load_setting()
    from blog.models import PostModel
    from gallery.models import ImageModel
    # 获取静态目录的位置（根据自己项目设置路径）
    p_img_folder = os.path.join(BASE_DIR, 'uploads/article')
    g_img_folder = os.path.join(BASE_DIR, 'uploads/gallery')

    # 查找该目录下的图片文件
    patterns = ['*.jpg', '*.png', '*.gif']
    p_imgs_del = 0
    p_imgs_count = 0
    g_imgs_del = 0
    g_imgs_count = 0

    for root, dirs, files in os.walk(p_img_folder):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                # 判断文件是否被使用(content字段是否包含filename)
                if PostModel.objects.filter(image__contains=filename).count() == 0:
                    img_path = os.path.join(root, filename)
                    os.remove(img_path)
                    p_imgs_del += 1
                p_imgs_count += 1
    for root, dirs, files in os.walk(g_img_folder):
        for pattern in patterns:
            for filename in fnmatch.filter(files, pattern):
                if ImageModel.objects.filter(image__contains=filename).count() == 0:
                    img_path = os.path.join(root, filename)
                    os.remove(img_path)
                    g_imgs_del += 1
                g_imgs_count += 1

    print('Post has %s images, delete %s images' % (p_imgs_count, p_imgs_del))
    print('Gallery has %s images, delete %s images' % (g_imgs_count, g_imgs_del))


if __name__ == '__main__':
    main()