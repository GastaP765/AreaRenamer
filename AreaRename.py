import maya.cmds as mc

Acode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
Ncode = '123456789'

def processing():
    sl_name = mc.ls(sl=True)
    core = mc.ls(sl=True)
    cnt = len(core)

    name = mc.textFieldGrp(txt, q=True, text=True)
    mode = mc.radioCollection(rC1, q=True, select=True)
    BandA = mc.radioCollection(rC2, q=True, select=True)
    type = mc.radioCollection(rC3, q=True, select=True)

    if mode == 'mode_add':
        if BandA == 'Before':
            for i in range(cnt):
                mc.rename(sl_name[i], name + '_' + sl_name[i])

        elif BandA == 'After':
            for i in range(cnt):
                mc.rename(sl_name[i], sl_name[i] + '_' + name)

    elif mode == 'mode_serial':
        if type == 'Alpha':
            for i in range(cnt):
                mc.rename(sl_name[i], name + Acode[i])
        elif type == 'Num':
            for i in range(cnt):
                mc.rename(sl_name[i], name + Ncode[i])


win = mc.window(t='AreaRenamer', widthHeight=(300,200))

colum = mc.columnLayout()

mc.rowLayout(nc=2)
rC1 = mc.radioCollection()
mode_add = mc.radioButton('mode_add', l='add', select=True, onc='add_mode()')
mode_serial = mc.radioButton('mode_serial', l='serial', onc='serial_mode()')
mc.setParent('..')

mc.rowLayout(nc=2)
rC2 = mc.radioCollection()
Before = mc.radioButton('Before', l='Before', select=True)
After = mc.radioButton('After', l='After')
mc.setParent('..')

mc.rowLayout(nc=2)
rC3 = mc.radioCollection()
Alpha = mc.radioButton('Alpha', l='Alphabet', select=True)
Num = mc.radioButton('Num', l='Number')
mc.setParent('..')

txt = mc.textFieldGrp(l='name:', ed=True, pht='please input text...')
mc.button(l='Done', c='processing()')

mc.showWindow()
