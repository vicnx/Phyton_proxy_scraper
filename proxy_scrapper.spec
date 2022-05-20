# -*- mode: python ; coding: utf-8 -*-

import sys
import site
from os import path
site_packages = next(p for p in sys.path if 'site-packages' in p)
block_cipher = None

url_sites_packages= site.getsitepackages()[1]
print(url_sites_packages)


a = Analysis(
    ['proxy_scrapper.py'],
    pathex=[url_sites_packages, 'C:\\proxy_scrapper'],
    binaries=[],
    datas=[(path.join(site_packages,"customtkinter"),"customtkinter"),(path.join(site_packages,"tksvg"),"tksvg")],
    hiddenimports=['customtkinter','tksvg'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='proxy_scrapper',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
