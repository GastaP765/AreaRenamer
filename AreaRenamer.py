import maya.cmds as mc

Acode = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def rename():
	sl_name = mc.ls(sl=True)
	cnt = len(sl_name)

	e = 0
	f = 0
	g = 0
	t = ''
	h = ''
	ns1 = '_'
	ns2 = '_'

	frn = mc.textField(name1, q=True, text=True)
	ctn = mc.textField(name2, q=True, text=True)
	afn = mc.textField(name3, q=True, text=True)
	aon = mc.radioCollection(rc1, q=True, select=True)

	if frn == '':
		ns1 = ''
	if afn == '':
		ns2 = ''
	if ctn == '':
		mc.warning('Base name is not specified')

	if aon == 'alp':
		for i in sl_name:
			mc.rename(i, frn + ns1 + ctn + h + t + Acode[e] + ns2 + afn)
			if e == 25:
				e = 0
				if t == '':
					t = Acode[f]
				else:
					if f == 25:
						f = 0
						if h == '':
							h = Acode[g]
						else:
							g = g + 1
							h = Acode[g]
					else:
						f = f + 1
						t = Acode[f]
			else:
				e = e + 1

	elif aon == 'num':
		for i in range(cnt):
			j = str(i+1)
			mc.rename(sl_name[i], frn + ns1 + ctn + j + ns2 + afn)


if mc.window('AreaRenamer', exists=True):
	mc.deleteUI('AreaRenamer')

win = mc.window('AreaRenamer', t='AreaRenamer', mxb=False, widthHeight=(300,150))
mc.columnLayout(adj=True)

mc.frameLayout(l='Serial, Alphabet or Number')
mc.rowLayout(nc=2, cat=[(1, 'left',50), (2, 'left', 50)])
rc1 = mc.radioCollection()
rb1 = mc.radioButton('alp', l='Alphabet', sl=True,)
rb2 = mc.radioButton('num', l='Number')
mc.setParent('..')

mc.frameLayout(l='setName')
mc.rowLayout(nc=5, cw5=(95, 5, 95, 5, 95))
name1 = mc.textField('name1', w=95, pht='BeforeName')
mc.text(l='_')
name2 = mc.textField('name2', w=95, pht='BaceName')
mc.text(l='_')
name3 = mc.textField('name3', w=95, pht='AfterName')
mc.setParent('..')

mc.button(w=200, h=30, l='rename', c='rename()')

mc.showWindow(win)
