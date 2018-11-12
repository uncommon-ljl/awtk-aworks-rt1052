﻿#!/usr/bin/python

import os
import glob
import copy
import shutil
import platform


# XXX: make sure no no ascii chars in the path name.

AWTK_ROOT_DIR = 'E:/zlgopen/awtk';
PORT_ROOT_DIR = os.getcwd();
DST_ROOT_DIR = 'E:/zlgopen/awtk-aworks-rt1052/output';
NANOVG_BACKEND = 'AGGE'


def joinPath(root, subdir):
  return os.path.normpath(os.path.join(root, subdir))

def copyFile(src_root_dir, src, dst_root_dir, dst):
    s = joinPath(src_root_dir, src)
    d = joinPath(dst_root_dir, dst)
    print(s + '->' + d)
    dir=os.path.dirname(d)
    if os.path.exists(dir):
        shutil.copyfile(s, d)
    else:
        os.makedirs(dir)
        shutil.copyfile(s, d)

def copyAwtkFile(src, dst):
    copyFile(AWTK_ROOT_DIR, src, DST_ROOT_DIR, dst)

def copyPortFile(src, dst):
    copyFile(PORT_ROOT_DIR, src, DST_ROOT_DIR, dst)

def copyFiles(src_root_dir, src, dst_root_dir, dst):
    s = joinPath(src_root_dir, src)
    d = joinPath(dst_root_dir, dst)
    print(s + '->' + d)
    shutil.rmtree(d, True)
    shutil.copytree(s, d, ignore=shutil.ignore_patterns("*.obj"))

def copyAwtkFiles(src, dst):
    copyFiles(AWTK_ROOT_DIR, src, DST_ROOT_DIR, dst)

def copyPortFiles(src, dst):
    copyFiles(PORT_ROOT_DIR, src, DST_ROOT_DIR, dst)


copyAwtkFiles('3rd/stb', 'awtk/3rd/stb')
copyAwtkFiles('3rd/libunibreak', 'awtk/3rd/libunibreak')
copyAwtkFiles('3rd/gpinyin/src', 'awtk/3rd/gpinyin/src')
copyAwtkFiles('3rd/gpinyin/include', 'awtk/3rd/gpinyin/include')

copyAwtkFiles('3rd/nanovg/base', 'awtk/3rd/nanovg/base')
if NANOVG_BACKEND == 'AGG':
  copyAwtkFiles('3rd/agg', 'awtk/3rd/agg')
  copyAwtkFiles('3rd/nanovg/agg', 'awtk/3rd/nanovg/agg')
elif NANOVG_BACKEND == 'AGGE':
  copyAwtkFiles('3rd/agge', 'awtk/3rd/agge')
  copyAwtkFiles('3rd/nanovg/agge', 'awtk/3rd/nanovg/agge')
else:
  assert 0, "NANOVG_BACKEND != {AGG, AGGE}"


copyAwtkFiles('src/misc', 'awtk/src/misc')
copyAwtkFiles('src/xml', 'awtk/src/xml')
copyAwtkFiles('src/base', 'awtk/src/base')
copyAwtkFiles('src/font_loader', 'awtk/src/font_loader')
copyAwtkFiles('src/blend', 'awtk/src/blend')
copyAwtkFiles('src/ui_loader', 'awtk/src/ui_loader')
copyAwtkFiles('src/image_loader', 'awtk/src/image_loader')
copyAwtkFiles('src/ext_widgets', 'awtk/src/ext_widgets')
copyAwtkFiles('src/widget_animators', 'awtk/src/widget_animators')

copyAwtkFile('src/awtk.c', 'awtk/src/awtk.c')
copyAwtkFile('src/awtk.h', 'awtk/src/awtk.h')
copyAwtkFile('src/vgcanvas/vgcanvas_nanovg_soft.c', 'awtk/src/vgcanvas/vgcanvas_nanovg_soft.c')
copyAwtkFile('src/vgcanvas/vgcanvas_nanovg_soft.inc', 'awtk/src/vgcanvas/vgcanvas_nanovg_soft.inc')

LCD_FILES=['lcd_mem.h',
    'lcd_mem.inc',
    'lcd_mem_rgba8888.h',
    'lcd_mem_rgba8888.c',
    'lcd_mem_bgra8888.h',
    'lcd_mem_bgra8888.c',
    'lcd_mem_bgr565.h',
    'lcd_mem_bgr565.c']
for f in LCD_FILES:
    sfilename=os.path.join('src/lcd/', f);
    dfilename=os.path.join('awtk/src/lcd/', f);
    copyAwtkFile(sfilename, dfilename)

INPUT_METHODS_FILES=['input_engines/input_engine_pinyin.cpp',
    'input_methods/input_method_creator.c',
    'input_methods/input_method_default.inc',
    'input_methods/input_method_null.inc',
    'input_methods/suggest_words.inc']
for f in INPUT_METHODS_FILES:
    sfilename=os.path.join('src/', f);
    dfilename=os.path.join('awtk/src/', f);
    copyAwtkFile(sfilename, dfilename)

MAIN_LOOP_FILES=['main_loop_simple.h',
    'main_loop_simple.c',
    'main_loop_raw.inc']
for f in MAIN_LOOP_FILES:
    sfilename=os.path.join('src/main_loop', f);
    dfilename=os.path.join('awtk/src/main_loop', f);
    copyAwtkFile(sfilename, dfilename)

WINDOW_ANIMATORS_FILES=['bottom_to_top.inc',
    'top_to_bottom.inc',
    'center_scale.inc',
    'vtranslate.inc',
    'common.inc',
    'window_animator_fb.c',
    'fade.inc',
    'htranslate.inc']
for f in WINDOW_ANIMATORS_FILES:
    sfilename=os.path.join('src/window_animators', f);
    dfilename=os.path.join('awtk/src/window_animators', f);
    copyAwtkFile(sfilename, dfilename)


copyAwtkFiles('demos/assets', 'awtk-demos/assets')

DEMO_FILES=['assets.h',
    'assets.c',
    'demo_main.c',
    'demo_ui_app.c',
    'common.inc']
for f in DEMO_FILES:
    sfilename=os.path.join('demos', f);
    dfilename=os.path.join('awtk-demos/', f);
    copyAwtkFile(sfilename, dfilename)


copyPortFiles('awtk-port', 'awtk-port')
copyPortFiles('pxp', 'pxp')
# copyPortFile('user_code/main.c', 'awtk-demos/main.c')	
