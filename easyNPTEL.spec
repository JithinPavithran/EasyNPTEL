# -*- mode: python -*-

block_cipher = None


a = Analysis(['easyNPTEL.py'],
             pathex=['/home/jithin/Documents/projects/EasyNPTEL'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='easyNPTEL',
          debug=False,
          strip=False,
          upx=True,
          console=True )
