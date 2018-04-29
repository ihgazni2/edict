import edict.edict as eded


bigd = {'key_4_ndHFNxbJx': 'v_7', 'key_2_fDuSOSq': 'v_3', 'key_5_bzRxPO': 'v_1', 'key_12_zWoEsZK': 'v_4', 'key_13_TNQhzLG': {'key_1_MMSpkENbML': 'v_4', 'key_2_': 'v_2'}, 'key_10_BlAymsk': 'v_5', 'key_8_mSwVqMQUi': 'v_6', 'key_9_xxhVI': 'v_1', 'key_6_XEEnXyYIYc': 'v_6', 'key_11_wnuZR': 'v_7', 'key_7_ULczdXwEkZ': 'v_5', 'key_1_jxJj': {'key_2_WFWeHeK': 'v_4', 'key_3_yMc': {'key_8_wmwD': 'v_1', 'key_5_FaURnGkAq': 'v_8', 'key_1_RtFTeZp': 'v_3', 'key_2_uaHOVRmD': 'v_4', 'key_12_DLeflhpNff': 'v_2', 'key_10_dNq': 'v_7', 'key_3_MTJpL': {'key_8_UQMX': {'key_2_mN': 'v_3', 'key_1_MJa': 'v_2'}, 'key_10_EEm': 'v_4', 'key_5_Qxl': 'v_5', 'key_11_UUrsUZnK': 'v_1', 'key_2_X': 'v_3', 'key_9_mFaJBJNv': 'v_1', 'key_6_vojwlSD': 'v_2', 'key_4_GqdmzvXr': 'v_5', 'key_1_': 'v_8', 'key_3_gija': 'v_8', 'key_7_QIgv': 'v_7'}, 'key_11_oEkHcD': 'v_5', 'key_4_TM': 'v_8', 'key_7_wvcAtb': 'v_7', 'key_9_fECO': 'v_1', 'key_6_tjE': 'v_5'}, 'key_1_kg': 'v_6'}, 'key_15_ATsyhp': 'v_4', 'key_16_jrtxBTq': 'v_5', 'key_14_minJO': 'v_8', 'key_3_gdqWvs': 'v_5'}




#__init__.0.png
d = {1:'a',2:'b',3:'a'}
ed = eded.Edict(d)
ed

klist = [1,2,3]
vlist = ['a','b','a']
ed = eded.Edict(klist,vlist)
ed


#__repr__.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed

#ktree.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ktree = ed.ktree()
tmp = eded.show_kmatrix(ktree)


#__getitem__.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed['x','yy','zz']
ed['u','a']

#__setitem__.0.png

d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed['x','yy','zz'] = 333
ed['u','a'] = 'WWW'
pobj(ed.dict)


#__delitem__.0.png

d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
del ed['x','yy','zz'] 
pobj(ed.dict)



#include_pathlist.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.include_pathlist('x','yy')
ed.include_pathlist('x','yy','zz')
ed.include_pathlist('x','yy','www')

#pathlists.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.pathlists()

#bracket_lists.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.bracket_lists()


#vksdesc.0.png

d = {'a':'v1','b':'v2','c':'v3','d':'v1'}
pobj(d)
ed = eded.Edict(d)
ed.keys_via_value('v1')


#vksdesc.0.png
d = {'a':'v1','b':'v2','c':'v3','d':'v1'}
pobj(d)
ed = eded.Edict(d)
ed.vksdesc()

#uniqualize.0.png
d = {1:'a',2:'b',3:'c',4:'b'}
pobj(d)
ed = eded.Edict(d)
ed2 = ed.uniqualize()
ed
ed2

ed = eded.Edict(d)
ed2 = ed.uniqualize(deepcopy=True)
ed
ed2



#extend.0.png extend.1.png
d1 = {1:'a',2:'b',3:'c',4:'d'}
d2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.extend(ed2)
ed1
ed3


d1 = {1:'a',2:'b',3:'c',4:'d'}
d2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed2.extend(ed1,deepcopy=True)
ed2
ed3


#update_intersection.0.png
d1 = {1:'a',2:'b',3:'c',4:'d'}
d2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.update_intersection(ed2,deepcopy=True)
ed3
ed1

ed3 = ed2.update_intersection(ed1)
ed3 
ed2 

#update.0.png  update.1.png

d1 = {1:'a',2:'b',3:'c',4:'d'}
d2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.update(ed2,deepcopy=True)
ed3
ed1


d1 = {1:'a',2:'b',3:'c',4:'d'}
d2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed2.update(ed1)
ed3 
ed2 


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@


#union.0.png


d1 = {'a':'x','b':'y','c':'z'}
d2 = {'a':'x','b':'u','d':'v'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.union(ed2)
ed3


#intersection.0.png
d1 = {'a':'x','b':'y','c':'z'}
d2 = {'a':'x','b':'u','d':'v'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.intersection(ed2)
ed3

#diff.0.png

d1 = {'a':'x','b':'y','c':'z'}
d2 = {'a':'x','b':'u','d':'v'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.diff(ed2)
ed3
ed3 = ed2.diff(ed1)
ed3



#complement.0.png

d1 = {'a':'x','b':'y','c':'z'}
d2 = {'a':'x','b':'u','d':'v'}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed3 = ed1.complement(ed2)
ed3
ed3 = ed2.complement(ed1)
ed3


#mirror.0.png
d1 = {'a':'x','b':'y','c':'z'}
ed1 = eded.Edict(d1)
ed1.mirrable()
ed1.mirror()

d2 = {'a':'x','b':'x','c':'z'}
ed2 = eded.Edict(d2)
ed2.mirrable()

#comprise.0.png

d1 = {'a':1,'b':2,'c':3,'d':4}
d2 = {'b':2,'c':3}
ed1 = eded.Edict(d1)
ed2 = eded.Edict(d2)
ed1.comprise(ed2)


#tlist.0.png
d1 = {'a':1,'b':2,'c':3,'d':4}
ed1 = eded.Edict(d1)
ed1.tlist()

#setdefault.0.png 

d1 = {'a':1,'b':{},'c':3}
ed1 = eded.Edict(d1)
ed1.setdefault('a','x')
ed1
ed1.setdefault('b','y')
ed1
ed1.setdefault('e','f','g')
ed1
ed1.setdefault('e','f','g','h')
ed1




#keys_via_value.0.png
#pathlists_via_value
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}


ed = eded.Edict(d)
ed.keys_via_value(20)

value = {
    'x2': 'x22',
    'x1': 'x11'
}
ed.keys_via_value(value)

ed.keys_via_value(20,from_lv=1,to_lv=2)
ed.keys_via_value(20,from_lv=2,to_lv=3)



#bracket_lists_via_value

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}


ed = eded.Edict(d)
ed.bracket_lists_via_value(20)

value = {
    'x2': 'x22',
    'x1': 'x11'
}
ed.bracket_lists_via_value(value)

ed.bracket_lists_via_value(20,from_lv=1,to_lv=2)
ed.bracket_lists_via_value(20,from_lv=2,to_lv=3)



#contains.0.png contains.1.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}

ed = eded.Edict(d)
ed.contains(20)
ed.contains(20,from_lv=1,to_lv=2)
ed.contains(20,from_lv=2,to_lv=3)
value = {
    'x2': 'x22',
    'x1': 'x11'
}
ed.contains(value)

#count.0.png  count.1.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}

ed = eded.Edict(d)
ed.count(20)
ed.count(20,from_lv=1,to_lv=2)
ed.count(20,from_lv=2,to_lv=3)
value = {
    'x2': 'x22',
    'x1': 'x11'
}
ed.count(value)


#klist.0.png  klist vlist kvlists
d = {1: {2: {22: 222}}, 3: {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.klist()
ed.vlist()
ed.kvlists()


#vnest.0.png 
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
vnest = ed.vnest()
tmp = eded.show_vmatrix(vnest)
vnest


#ktree_vnest.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.ktree_vnest()



#未完成
#kdescmat.0.png kdescmat.1.png

d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
kdmat = ed.kdescmat()

pobj(kdmat[1][0])

#
#vdescmat.0.png  vdescmat.1.png  vdescmat.2.png

d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
vdmat = ed.vdescmat()
pobj(vdmat[1][0])

#未完成
#kvdescmats.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
vdmat = ed.kvdescmats()


#dfs.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.kdfs()
ed.vdfs()
ed.dfses()

#wfs.0.png  
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.kwfs()
ed.vwfs()
ed.wfses()



#rvwfs.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.rvwfs()

#rvdfs.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
ed.rvdfs()

#rvmat.0.png
d = {'x': {'yy': {'zz': 222}}, 'u': {'a': 'b'}}
pobj(d)
ed = eded.Edict(d)
rvmat = ed.rvmat()
elel.forEach(rvmat,print)


#keypaths.0.png  keypaths.1.png  keypaths.2.png

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}

ed = eded.Edict(d)
kps = ed.keypaths()
elel.forEach(kps,print)
kps = ed.keypaths(2)
elel.forEach(kps,print)
kps = ed.keypaths(1,2)
elel.forEach(kps,print)


kps = ed.keypaths(2,4)
elel.forEach(kps,print)
kps = ed.keypaths(leaf_only=True)
elel.forEach(kps,print)
kps = ed.keypaths(non_leaf_only=True)
elel.forEach(kps,print)


#keys.0.png  keys.1.png

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}

ed = eded.Edict(d)
ed.keys()
ed.keys(2)
ed.keys(1,2)
ed.keys(2,4)
ed.keys(leaf_only=True)
ed.keys(non_leaf_only=True)




#values.0.png   values.1.png  values.2.png  values.3.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}

ed = eded.Edict(d)
ed.values()
ed.values(2)
ed.values(1,2)


vs = ed.values(2,4)
elel.forEach(vs,print)
vs = ed.values(leaf_only=True)
elel.forEach(vs,print)
vs = ed.values(non_leaf_only=True)
elel.forEach(vs,print)


kpls = ed.keypaths(2,3,leaf_only=True)
elel.forEach(kpls,print)
brls = elel.array_map(kpls,elel.pl2gs)
elel.forEach(brls,print)

vs = ed.values(2,3,leaf_only=True)
elel.forEach(vs,print)
eded.show_dict(d,brls)


######################################3
#depth.0.png
#total.0.png
#maxLevelWidth.0.png
#flatWidth.0.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}
ed = eded.Edict(d)
ed.depth()
ed.total()
ed.maxLevelWidth()
ed.flatWidth()



#tree.0.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}
ed = eded.Edict(d)
ed.tree()


#cond_select_key
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': 20,
 'u':
      {
       'u1': 20
      }
}


ed = eded.Edict(d)
ed.cond_select_key('x')
ed.cond_select_key('x',mode='strict')

regex= re.compile("[24]$")
ed.cond_select_key(regex)


def cond_func(ele,index):
    cond1 = (ele[-1]=='x2')
    cond2 = (ele.__len__() == 3)
    cond = (cond1 & cond2)
    return(cond)

ed.cond_select_key(cond_func)

#cond_select_leaf_value

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}

ed = eded.Edict(d)
ed.cond_select_leaf_value('x')
regex= re.compile("[24]$")
ed.cond_select_leaf_value(regex)

#cond_select_keypath
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}

ed = eded.Edict(d)
kdfs = ed.kdfs()
elel.forEach(kdfs,print)

ed.cond_select_keypath(['y2'])


#ancestors.0.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}

ed = eded.Edict(d)
keypath = ['y', 'xx', 'x2']

ed.ancestor_keypaths(keypath)
ed.ancestors(keypath)
ed['y', 'xx']
ed['y']

#parent.0.png

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}

ed = eded.Edict(d)
keypath = ['y', 'xx', 'x2']

ed.parent_keypath(keypath)
ed.parent(keypath)
ed['y', 'xx']


#descendants.0.png
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}


ed = eded.Edict(d)
keypath = ['y']


ed.descendant_keypaths(keypath)
ed.descendant_keypaths(keypath,leaf_only=True)
ed.descendant_keypaths(keypath,non_leaf_only=True)

ed.descendants(keypath)
ed.descendants(keypath,leaf_only=True)
ed.descendants(keypath,non_leaf_only=True)


#lsib.0.png
#try this in python 3.6, the dict in py3.6 is ordered
d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.prevSibPath(keypath)
ed.prevSibling(keypath)
ed.lsib_path(keypath)
ed.lsib(keypath)

#rsib.0.png

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.nextSibPath(keypath)
ed.nextSibling(keypath)
ed.rsib_path(keypath)
ed.rsib(keypath)
keypath = ['y','y2']
ed.nextSibPath(keypath)
ed.nextSibling(keypath)
ed.rsib_path(keypath)
ed.rsib(keypath)

#####################

# ├──42. lcin_path 
# ├──43. lcin 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y','y1']
ed.lcin_path(keypath)
ed.lcin(keypath)

# ├──44. rcin_path 
# ├──45. rcin 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['x','x1']
ed.rcin_path(keypath)
ed.rcin(keypath)


#
# ├──46. son_paths 
# ├──47. sons 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.son_paths(keypath)
ed.sons(keypath)


# ├──24. sib_paths 
# ├──25. sibs 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.sib_paths(keypath)
ed.sibs(keypath)


#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
# ├──26. someSibPaths 
# ├──27. someSibs 
# ├──28. some_sib_paths 
# ├──29. some_sibs 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.someSibPaths(keypath,0,2)
ed.some_sibs(keypath,0,2)


# ├──30. whichSibPath 
# ├──31. whichSib 
# ├──32. which_sib_path 
# ├──33. which_sib 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.which_sib_path(keypath,3)
ed.which_sib(keypath,3)



########################################
# ├──34. precedingSibPaths 
# ├──35. precedingSibs 
# ├──36. preceding_sib_paths 
# ├──37. preceding_sibs 

d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.preceding_sib_paths(keypath)
ed.preceding_sibs(keypath)



# ├──38. followingSibPaths 
# ├──39. followingSibs 
# ├──40. following_sib_paths 
# ├──41. following_sibs 


d = {
 'x':
      {
       'x2': 'x22',
       'x1': 'x11'
      },
 'y':
      {
       'y1': 'v1',
       'y2':
             {
              'y4': 'v4',
              'y3': 'v3',
             },
       'xx': 
            {
                'x2': 'x22',
                'x1': 'x11'
          }
      },
 't': "2a",
 'u':
      {
       'u1': "2a"
      }
}
d

ed = eded.Edict(d)
keypath = ['y']
ed.following_sib_paths(keypath)
ed.following_sibs(keypath)



############################













import edict.edict as eded
import elist.elist as elel


kt,vn = eded._d2kvmatrix(d)
rvmat = eded._get_rvmat(d)
depth = rvmat.__len__()
kdmat = eded._scankm(kt)
vndmat = eded._scanvm(vn)

keypath = ['y']

################


    

##################
################################################
# 需要等crtable 和ltdict 改造完毕
# crtable.max_cols_in_table_via_rows_dict(kdfs)
# cratble.padding_rows(kdfs)
################################################# 
