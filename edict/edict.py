import re
import copy
import elist.elist as elel

def _keys_via_value(d,v):
    '''
        d = {1:'a',2:'b',3:'a'}
        _keys_via_value(d,'a')
    '''
    rslt = []
    for key in d:
        if(d[key] == v):
            rslt.append(key)
    return(rslt)

def d2kvlist(d):
    '''
        d = {'GPSImgDirectionRef': 'M', 'GPSVersionID': b'\x02\x03\x00\x00', 'GPSImgDirection': (21900, 100)}
        pobj(d)
        kl,vl = d2kvlist(d)
        pobj(kl)
        pobj(vl)
    '''
    kl = list(d.keys())
    vl = list(d.values())
    return((kl,vl))

def kvlist2d(kl,vl):
    '''
    '''
    d = {}
    for i in range(0,kl.__len__()):
        k = kl[i]
        v = vl[i]
        d[k] = v
    return(d)

#dele dict-element

def dele2t(dele):
    '''
    '''
    k = list(d.keys())[0]
    v = list(d.values())[0]
    return((k,v))

def t2dele(t):
    '''
    '''
    return({t[0]:t[1]})

#_vksdesc value-keys-description
def _vksdesc(d):
    '''
        d = {'a':1,'b':2,'c':2,'d':4}
        desc = _vksdesc(d)
        pobj(desc)
    '''
    pt = copy.deepcopy(d)
    seqs_for_del =[]
    vset = set({})
    for k in pt:
        vset.add(pt[k])
    desc = {}
    for v in vset:
        desc[v] = []
    for k in pt:
        desc[pt[k]].append(k)
    return(desc)

#
def tlist2dict(tuple_list,**kwargs):
    '''
        #duplicate keys will lost
        tl = [(1,2),(3,4),(1,5)]
        tlist2dict(tl)
    '''
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(is_tlist(tuple_list)):
            pass
        else:
            return(None)
    else:
        pass
    j = {}
    if(deepcopy):
        new = copy.deepcopy(tuple_list)
    else:
        new = tuple_list
    for i in range(0,new.__len__()):
        temp = new[i]
        key = temp[0]
        value = temp[1]
        j[key] = value
    return(j)

def dict2tlist(this_dict,**kwargs):
    '''
        #sequence will be losted
        d = {'a':'b','c':'d'}
        dict2tlist(d)
    '''
    if('check' in kwargs):
        check = kwargs['check']
    else:
        check = 1
    if(check):
        if(isinstance(this_dict,dict)):
            pass
        else:
            return(None)
    else:
        pass
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    tuple_list = []
    if(deepcopy):
        new = copy.deepcopy(this_dict)
    else:
        new = this_dict
    i = 0
    for key in this_dict:
        value = this_dict[key]
        tuple_list.append((key,value))
    return(tuple_list)

###

def is_mirrable(d):
    '''
        d = {1:'a',2:'a',3:'b'}
    '''
    vl = list(d.values())
    lngth1 = vl.__len__()
    uvl = elel.uniqualize(vl)
    lngth2 = uvl.__len__()
    cond = (lngth1 == lngth2)
    return(cond)

def dict_mirror(d,**kwargs):
    '''
        d = {1:'a',2:'a',3:'b'}
    '''
    md = {}
    if('sort_func' in kwargs):
        sort_func = kwargs['sort_func']
    else:
        sort_func = sorted
    vl = list(d.values())
    uvl = elel.uniqualize(vl)
    for v in uvl:
        kl = _keys_via_value(d,v)
        k = sorted(kl)[0]
        md[v] = k
    return(md)

def _text_cond(text,condmatch,*args):
    if(type(condmatch)==type("")):
        if(condmatch in text):
            return(True)
        else:
            return(False)
    elif(type(condmatch) == type(re.compile(""))):
        m = condmatch.search(text)
        if(m):
            return(True)
        else:
            return(False)
    else:
        return(condmatch(text,*args))

def _cond_select_via_key(d,cond_match=None,**kwargs):
    '''
        d = {
            "ActiveArea":"50829", 
            "Artist":"315",                 
            "AsShotPreProfileMatrix":"50832",
            "AnalogBalance":"50727",          
            "AsShotICCProfile":"50831",       
            "AsShotProfileName":"50934",
            "AntiAliasStrength":"50738",      
            "AsShotNeutral":"50728",          
            "AsShotWhiteXY":"50729"
        }
        _cond_select_via_key(d,"An")
        _cond_select_via_key(d,"As")
        regex = re.compile("e$")
        _cond_select_via_key(d,regex)
    '''
    if('cond_func' in kwargs):
        cond_func = kwargs['cond_func']
    else:
        cond_func = _text_cond
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    rslt = {}
    for key in d:
        if(cond_func(key,cond_match,*cond_func_args)):
            rslt[key] = d[key]
        else:
            pass
    return(rslt)

def _cond_select_via_value(d,cond_match=None,**kwargs):
    '''
        d = {
            "ActiveArea":"50829", 
            "Artist":"315",                 
            "AsShotPreProfileMatrix":"50832",
            "AnalogBalance":"50727",          
            "AsShotICCProfile":"50831",       
            "AsShotProfileName":"50934",
            "AntiAliasStrength":"50738",      
            "AsShotNeutral":"50728",          
            "AsShotWhiteXY":"50729"
        }
        _cond_select_via_value(d,"50")
        _cond_select_via_value(d,"72")
        regex = re.compile("8$")
        _cond_select_via_value(d,regex)
    '''
    if('cond_func' in kwargs):
        cond_func = kwargs['cond_func']
    else:
        cond_func = _text_cond
    if('cond_func_args' in kwargs):
        cond_func_args = kwargs['cond_func_args']
    else:
        cond_func_args = []
    rslt = {}
    for key in d:
        value = d[key]
        if(cond_func(value,cond_match,*cond_func_args)):
            rslt[key] = d[key]
        else:
            pass
    return(rslt)


def _diff_internal(d1,d2):
    '''
        d1 = {'a':'x','b':'y','c':'z'}
        d2 = {'a':'x','b':'u','d':'v'}
        _diff_internal(d1,d2)
        _diff_internald2,d1)
    '''
    same =[]
    kdiff =[]
    vdiff = []
    for key in d1:
        value = d1[key]
        if(key in d2):
            if(value == d2[key]):
                same.append(key)
            else:
                vdiff.append(key)
        else:
            kdiff.append(key)
    return({'same':same,'kdiff':kdiff,'vdiff':vdiff})

#并集
def _union(d1,d2):
    '''
        d1 = {'a':'x','b':'y','c':'z'}
        d2 = {'a':'x','b':'u','d':'v'}
        _union(d1,d2)
        _union(d2,d1)
    '''
    u = {}
    ds = _diff_internal(d1,d2)
    for key in ds['same']:
        u[key] = d1[key]
    for key in ds['vdiff']:
        u[key] = d1[key]
    for key in ds['kdiff']:
        u[key] = d1[key]
    ds = _diff_internal(d2,d1)
    for key in ds['kdiff']:
        u[key] = d2[key]
    return(u)


#差集
def _diff(d1,d2):
    '''
        d1 = {'a':'x','b':'y','c':'z'}
        d2 = {'a':'x','b':'u','d':'v'}
        _diff(d1,d2)
        _diff(d2,d1)
    '''
    d = {}
    ds = _diff_internal(d1,d2)
    for key in ds['vdiff']:
        d[key] = d1[key]
    for key in ds['kdiff']:
        d[key] = d1[key]
    return(d)

#交集

def _intersection(d1,d2):
    '''
        d1 = {'a':'x','b':'y','c':'z'}
        d2 = {'a':'x','b':'u','d':'v'}
        _intersection(d1,d2)
        _intersection(d2,d1)
    '''
    i = {}
    ds = _diff_internal(d1,d2)
    for key in ds['same']:
        i[key] = d1[key]
    return(i)

#补集
def _complement(d1,d2):
    '''
        d1 = {'a':'x','b':'y','c':'z'}
        d2 = {'a':'x','b':'u','d':'v'}
        complement(d1,d2)
        complement(d2,d1)
    '''
    u = _union(d1,d2)
    c = _diff(u,d1)
    return(c)

def _uniqualize(d):
    '''
        d = {1:'a',2:'b',3:'c',4:'b'}
        _uniqualize(d)
    '''
    pt = copy.deepcopy(d)
    seqs_for_del =[]
    vset = set({})
    for k in pt:
        vset.add(pt[k])
    tslen = vset.__len__()
    freq = {}
    for k in pt:
        v = pt[k]
        if(v in freq):
            freq[v] = freq[v] + 1
            seqs_for_del.append(k)
        else:
            freq[v] = 0
    npt = {}
    for k in pt:
        if(k in seqs_for_del):
            pass
        else:
            npt[k] = pt[k]
    pt = npt
    return(npt)

def _extend(dict1,dict2,**kwargs):
    '''
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        d = _extend(dict1,dict2)
        pobj(d)
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        d = _extend(dict1,dict2,overwrite=1)
        pobj(d)
    '''
    if('deepcopy' in kwargs):
        deepcopy=kwargs['deepcopy']
    else:
        deepcopy=1
    if('overwrite' in kwargs):
        overwrite=kwargs['overwrite']
    else:
        overwrite=0
    if(deepcopy):
        dict1 = copy.deepcopy(dict1)
        dict2 = copy.deepcopy(dict2)
    else:
        pass
    d = dict1
    for key in dict2:
        if(key in dict1):
            if(overwrite):
                d[key] = dict2[key]
            else:
                pass
        else:
            d[key] = dict2[key]
    return(d)

def _comprise(dict1,dict2):
    '''
        dict1 = {'a':1,'b':2,'c':3,'d':4}
        dict2 = {'b':2,'c':3}
        _comprise(dict1,dict2)
    '''
    len_1 = dict1.__len__()
    len_2 = dict2.__len__()
    if(len_2>len_1):
        return(False)
    else:
        for k2 in dict2:
            v2 = dict2[k2]
            if(k2 in dict1):
                v1 = dict1[k2]
                if(v1 == v2):
                    return(True)
                else:
                    return(False)
            else:
                return(False)

#@@@@@@@@@@@@@@@@@@@@
def _update_intersection(dict1,dict2,**kwargs):
    '''
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        _update_intersection(dict1,dict2)
        pobj(dict1)
        pobj(dict2)
    '''
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if(deepcopy == 1):
        dict1 = copy.deepcopy(dict1)
    else:
        pass
    for key in dict2:
        if(key in dict1):
            dict1[key] = dict2[key]
    return(dict1)

def _update(dict1,dict2,**kwargs):
    '''
        dict1 = {1:'a',2:'b',3:'c',4:'d'}
        dict2 = {5:'u',2:'v',3:'w',6:'x',7:'y'}
        _update(dict1,dict2)
        pobj(dict1)
        pobj(dict2)
    '''
    if('deepcopy' in kwargs):
        deepcopy = kwargs['deepcopy']
    else:
        deepcopy = 1
    if(deepcopy == 1):
        dict1 = copy.deepcopy(dict1)
    else:
        pass
    dict1 = _extend(dict1,dict2,overwrite=True)
    return(dict1)

#important and special func
#给elist 添加个类似方法
def _setdefault_via_pathlist(external_dict,path_list,**kwargs):
    '''
        #if path_list already in external_dict, will do nothing
        y = {}
        path_list = ['c','b']
        _setdefault_via_pathlist(y,path_list)
        y
        _setdefault_via_pathlist(y,path_list)
        y = {}
        _setdefault_via_pathlist(y,path_list)
        y
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    if('default_element' in kwargs):
        default_element = kwargs['default_element']
    else:
        default_element = {}
    this = external_dict
    for i in range(0,path_list.__len__()):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        try:
            this.__getitem__(key)
        except:
            try:
                # necessary ,when default_element = {} or []
                de = copy.deepcopy(default_element)
                this.__setitem__(key,de)
            except:
                return(external_dict)
            else:
                pass
            this = this.__getitem__(key)
        else:
            this = this.__getitem__(key)
    return(external_dict)


#for array_map
def _setdefault_via_pathlist2(path_list,external_dict,**kwargs):
    return(_setdefault_via_pathlist(external_dict,path_list,,**kwargs))


def _setitem_via_pathlist(external_dict,path_list,value,**kwargs):
    '''
        y = {'c': {'b': {}}}
        _setitem_via_pathlist(y,['c','b'],200)
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    this = external_dict
    for i in range(0,path_list.__len__()-1):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        this = this.__getitem__(key)
    this.__setitem__(path_list[-1],value)
    return(external_dict)

#for array_map
def _setitem_via_pathlist2(path_list,external_dict,**kwargs):
    return(_setitem_via_pathlist(external_dict,path_list,,**kwargs))



def _getitem_via_pathlist(external_dict,path_list,**kwargs):
    '''
        y = {'c': {'b': 200}}
        _getitem_via_pathlist(y,['c','b'])
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    this = external_dict
    for i in range(0,path_list.__len__()):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        this = this.__getitem__(key)
    return(this)

#for array_map
def _getitem_via_pathlist2(path_list,external_dict,**kwargs):
    return(_getitem_via_pathlist(external_dict,path_list,,**kwargs))


#special 
def _delitem_via_pathlist(external_dict,path_list,**kwargs):
    '''
        y = {'c': {'b': 200}}
        _delitem_via_pathlist(y,['c','b'])
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    this = external_dict
    for i in range(0,path_list.__len__()-1):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        this = this.__getitem__(key)
    this.__delitem__(path_list[-1])
    return(external_dict)


#for array_map
def _delitem_via_pathlist2(path_list,external_dict,**kwargs):
    return(_delitem_via_pathlist(external_dict,path_list,,**kwargs))



def _include_pathlist(external_dict,path_list,**kwargs):
    '''
        y = {
            'a':
                {'x':88},
            'b':
                {
                    'x':
                        {'c':66}
                }
        }
        _include_pathlist(y,['a'])
        _include_pathlist(y,['a','x'])
        _include_pathlist(y,['b','x','c'])
    '''
    if('s2n' in kwargs):
        s2n = kwargs['s2n']
    else:
        s2n = 0
    if('n2s' in kwargs):
        n2s = kwargs['n2s']
    else:
        n2s = 0
    this = external_dict
    for i in range(0,path_list.__len__()):
        key = path_list[i]
        if(n2s ==1):
            key = str(key)
        if(s2n==1):
            try:
                int(key)
            except:
                pass
            else:
                key = int(key)
        try:
            this = this.__getitem__(key)
        except:
            return(False)
        else:
            pass
    return(True)

################

def max_word_width(myDict):
    '''
        currd = {0:'AutoPauseSpeed', 125:'HRLimitLow', 6:'Activity'}
        max_wordwidth(currd)
    '''
    maxValueWidth = 0
    for each in myDict:
        eachValueWidth = myDict[each].__len__()
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)

def max_display_width(myDict):
    '''
        currd = {0:'你们大家好', 125:'ABCDE', 6:'1234567'}
        dict_get_max_word_displaywidth(currd)
    '''
    maxValueWidth = 0
    for each in myDict:
        eachValueWidth = str_display_width(myDict[each])
        if(eachValueWidth > maxValueWidth):
            maxValueWidth = eachValueWidth
    return(maxValueWidth)


############################
###for nexted

def is_dict(obj):
    '''
        from edict.edict import *
        is_dict({1:2})
        is_dict(200)
    '''
    if(type(obj)==type({})):
        return(True)
    else:
        return(False)

def is_leaf(obj):
    '''
        the below is for nested-dict
        any type is not dict will be treated as a leaf
        empty dict will be treated as a leaf
        from edict.edict import *
        is_leaf(1)
        is_leaf({1:2})
        is_leaf({})
    '''
    if(is_dict(obj)):
        length = obj.__len__()
        if(length == 0):
            return(True)
        else:
            return(False)
    else:
        return(True)

def _gen_sonpl(ele,ppl):
    nppl = copy.deepcopy(ppl)
    nppl.append(ele)
    return(nppl)

def _new_ele_desc():
    '''
    '''
    desc = {
        'leaf':None,
        'depth':None,
        'breadth':None,
        'breadth_path':None,
        'sib_seq':None,
        'path':None,
        'parent_path':None,
        'parent_breadth':None,
        'parent_breadth_path':None,
        'lsib_path':None,
        'rsib_path':None,
        'lcin_path':None,
        'rcin_path':None,
        'sons_count':None,
        'leaf_son_paths':None,
        'non_leaf_son_paths':None,
        'leaf_descendant_paths':None,
        'non_leaf_descendant_paths':None,
        'flat_offset':None,
        'flat_len':None
    }
    return(desc)

def _d2kvmatrix(d):
    '''
        d = {1: 2, 3: {'a': 'b'}}
        km,vm = _d2kvmatrix(d)
        d = {1: {2:{22:222}}, 3: {'a': 'b'}}
        km,vm = _d2kvmatrix(d)
    '''
    km = []
    vm = [list(d.values())]
    vm_history ={0:[0]}
    unhandled = [{'data':d,'kpl':[]}]
    while(unhandled.__len__()>0):
        next_unhandled = []
        keys_level = []
        next_vm_history = {}
        for i in range(0,unhandled.__len__()):
            data = unhandled[i]['data']
            kpl = unhandled[i]['kpl']
            values = list(data.values())
            _setitem_via_pathlist(vm,vm_history[i],values)
            vm_pl = vm_history[i]
            del vm_history[i]
            keys = data.keys()
            keys = elel.array_map(keys,_gen_sonpl,kpl)
            keys_level.extend(keys)
            for j in range(0,values.__len__()):
                v = values[j]
                cond = is_leaf(v)
                if(cond):
                    pass
                else:
                    kpl = copy.deepcopy(keys[j])
                    next_unhandled.append({'data':v,'kpl':kpl})
                    vpl = copy.deepcopy(vm_pl)
                    vpl.append(j)
                    next_vm_history[next_unhandled.__len__()-1] = vpl
        vm_history = next_vm_history
        km.append(keys_level)
        unhandled = next_unhandled
    vm = vm[0]
    return((km,vm))

def show_kmatrix(km):
    '''
        d = {1: {2: {22: 222}}, 3: {'a': 'b'}}
        km = [[[1], [3]], [[1, 2], [3, 'a']], [[1, 2, 22]]]
        show_kmatrix(km)
    '''
    rslt = []
    for i in range(0,km.__len__()):
        level = km[i]
        for j in range(0,level.__len__()):
            kpl = level[j]
            print(kpl)
            rslt.append(kpl)
    return(rslt)

def show_vmatrix(vm):
    '''
        d = {1: {2: {22: 222}}, 3: {'a': 'b'}}
        vm = [[[222]], ['b']]
        show_vmatrix(vm)
    '''
    unhandled = vm
    while(unhandled.__len__()>0):
        next_unhandled = []
        for i in range(0,unhandled.__len__()):
            ele = unhandled[i]
            print(ele)
            cond = elel.is_leaf(ele)
            if(cond):
                pass
            else:
                children = ele[0]
                next_unhandled.append(children)
        unhandled = next_unhandled

def show_kmatrix_as_getStr(km):
    rslt = []
    for i in range(0,km.__len__()):
        level = km[i]
        for j in range(0,level.__len__()):
            kpl = level[j]
            gs = elel.pathlist_to_getStr(kpl)
            print(gs)
            rslt.append(gs)
    return(rslt)

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@

def _init_descmat_root():
    '''
    '''
    root = _new_ele_desc()
    root['depth'] = 0
    root['leaf'] = False
    root['breadth_path'] =[]
    root['path'] = []
    root['parent_path'] = []
    root['parent_breadth_path'] = []
    return(root)

def _init_descmat_via_km(km,descmat=[]):
    '''
    '''
    descmat_len = descmat.__len__()
    cond = (descmat_len == 0)
    depth = km.__len__()
    for i in range(0,depth):
        klevel = km[i]
        lngth = klevel.__len__()
        dlevel = elel.init(lngth,default_element=_new_ele_desc())
        if(cond):
            descmat.append(dlevel)
        else:
            pass
    descmat = elel.prepend(descmat,[_init_descmat_root()])
    return(descmat)

def _descmat_leaf_handler(desc,pdesc):
    '''
    '''
    desc['leaf_son_paths'] = []
    desc['non_leaf_son_paths'] = []
    desc['leaf_descendant_paths'] = []
    desc['non_leaf_descendant_paths'] = []
    kpl = desc['path']
    ####
    cpkpl = copy.deepcopy(kpl)
    if(pdesc['leaf_son_paths'] == None):
        pdesc['leaf_son_paths'] = [cpkpl]
    else:
        pdesc['leaf_son_paths'].append(cpkpl)
    ####
    if(pdesc['non_leaf_son_paths'] == None):
        pdesc['non_leaf_son_paths'] = []
    else:
        pass
    ####
    cpkpl = copy.deepcopy(kpl)
    if(pdesc['leaf_descendant_paths'] == None):
        pdesc['leaf_descendant_paths'] = [cpkpl]
    else:
        pdesc['leaf_descendant_paths'].append(cpkpl)
    ####
    if(pdesc['non_leaf_descendant_paths'] == None):
        pdesc['non_leaf_descendant_paths'] = []
    else:
        pass

def _descmat_non_leaf_handler(desc,pdesc):
    '''
    '''
    kpl = desc['path']
    ####
    cpkpl = copy.deepcopy(kpl)
    if(pdesc['non_leaf_son_paths'] == None):
        pdesc['non_leaf_son_paths'] = [cpkpl]
    else:
        pdesc['non_leaf_son_paths'].append(cpkpl)
    ####
    if(pdesc['leaf_son_paths'] == None):
        pdesc['leaf_son_paths'] = []
    else:
        pass
    ####
    cpkpl = copy.deepcopy(kpl)
    ldpl = desc['leaf_descendant_paths']
    cpldpl = copy.deepcopy(ldpl)
    nldpl = desc['non_leaf_descendant_paths']
    cpnldpl = copy.deepcopy(nldpl)
    if(pdesc['leaf_descendant_paths'] == None):
        pdesc['leaf_descendant_paths'] = cpldpl
    else:
        pdesc['leaf_descendant_paths'].extend(cpldpl)
    if(pdesc['non_leaf_descendant_paths'] == None):
        pdesc['non_leaf_descendant_paths'] = cpnldpl
        pdesc['non_leaf_descendant_paths'].append(cpkpl)
    else:
        pdesc['non_leaf_descendant_paths'].extend(cpldpl)
        pdesc['non_leaf_descendant_paths'].append(cpkpl)

def _acc_sons_count(desc):
    if(desc['leaf_son_paths'] == None):
        desc['leaf_son_paths'] = []
    else:
        pass
    if(desc['non_leaf_son_paths'] == None):
        desc['non_leaf_son_paths'] = []
    else:
        pass
    lscnt = desc['leaf_son_paths'].__len__()
    nlscnt = desc['non_leaf_son_paths'].__len__()
    return(lscnt + nlscnt)

def _scankm(km,descmat=[]):
    '''
    '''
    descmat = _init_descmat_via_km(km,descmat=descmat)
    depth = km.__len__()
    klevel = km[depth - 1]
    lngth = klevel.__len__()
    dlevel = descmat[depth]
    pdlevel = descmat[depth-1]
    for j in range(0,lngth):
        kpl = klevel[j]
        desc = dlevel[j]
        desc['leaf'] = True
        desc['depth'] = depth 
        desc['path'] = kpl
        desc['breadth'] = j 
        desc['sons_count'] = 0 
        desc['leaf_son_paths'] = []
        desc['non_leaf_son_paths'] = []
        desc['leaf_descendant_paths'] = []
        desc['non_leaf_descendant_paths'] = []
        pkpl = copy.deepcopy(kpl)
        pkpl.pop(-1)
        desc['parent_path'] = pkpl
        pbreadth = km[depth-2].index(pkpl)
        desc['parent_breadth'] = pbreadth
        ######
        pdesc = pdlevel[pbreadth]
        _descmat_leaf_handler(desc,pdesc)
    ####
    for i in range(depth-2,0,-1):
        level = i 
        klevel = km[level]
        lngth = klevel.__len__()
        dlevel = descmat[level+1]
        pdlevel = descmat[level]
        for j in range(0,lngth):
            #
            #
            kpl = klevel[j]
            desc = dlevel[j]
            desc['depth'] = level + 1
            desc['path'] = kpl
            desc['breadth'] = j 
            desc['sons_count'] = _acc_sons_count(desc)
            if(desc['sons_count'] == 0):
                desc['leaf'] = True
            else:
                desc['leaf'] = False
            pkpl = copy.deepcopy(kpl)
            pkpl.pop(-1)
            desc['parent_path'] = pkpl
            pbreadth = km[level-1].index(pkpl)
            desc['parent_breadth'] = pbreadth
            ######
            pdesc = pdlevel[pbreadth]
            if(desc['leaf']):
                _descmat_leaf_handler(desc,pdesc)
            else:
                _descmat_non_leaf_handler(desc,pdesc)
    #####depth 1
    level = 0 
    klevel = km[level]
    lngth = klevel.__len__()
    dlevel = descmat[level+1]
    pdlevel = descmat[level]
    for j in range(0,lngth):
        #
        #
        kpl = klevel[j]
        desc = dlevel[j]
        desc['depth'] = level + 1
        desc['path'] = kpl
        desc['breadth'] = j 
        desc['sons_count'] = _acc_sons_count(desc)
        if(desc['sons_count'] == 0):
            desc['leaf'] = True
        else:
            desc['leaf'] = False
        pkpl = copy.deepcopy(kpl)
        pkpl.pop(-1)
        desc['parent_path'] = pkpl
        pdesc = pdlevel[0]
        if(desc['leaf']):
            _descmat_leaf_handler(desc,pdesc)
        else:
            _descmat_non_leaf_handler(desc,pdesc)
    #####root 
    desc = descmat[0][0]
    desc['sons_count'] = _acc_sons_count(desc)
    return(descmat)

cmdlines_tree = _scankm

def _mat_size(mat):
    '''
    '''
    size = 0
    depth = mat.__len__()
    for i in range(0,depth):
        level = mat[i]
        size = size + level.__len__()
    return(size)


#km 是一个广度优先的pathlist 存储二维矩阵
#vm 是一个嵌套矩阵
#ltree = elel.ListTree(vm) 
#ltree.tree() 是一个深度优先的 pathlist 一维数组 
#_mat_size(km) == ltree.tree().__len__()
#ltree.desc[0][0] 是根节点 
#km[i] 与 ltree.desc[i-1] 对应
#

def get_kmwfs(km):
    '''
    '''
    kmwfs = []
    for i in range(0,km.__len__()):
        level = km[i]
        for j in range(0,level.__len__()):
            kpl = level[j]
            kmwfs.append(kpl)
    return(kmwfs)

def get_kmdfs(km,vmwfs):
    '''
    '''
    kmwfs = get_kmwfs(km)
    kmdfs = elel.batsorted(vmwfs,kmwfs)[0]
    return(kmdfs)
    


#
def _scanvm(vm):
    ltree = elel.ListTree(vm)
    vdescmat = ltree.desc
    return(vdescmat)


#
def _scan(d):
    '''
    '''
    km,vm = _d2kvmatrix(d)
    kdescmat = _scankm(km)
    vdescmat = _scanvm(vm)
    return((kdescmat,vdescmat))


def _kvmatrix2d(km,vm):
    '''
        
        km = [[[1], [3]], [[1, 2], [3, 'a']], [[1, 2, 22]]]
        show_kmatrix(km)
        vm = [[[222]], ['b']]
        show_vmatrix(vm)
        
        d = _kvmatrix2d(km,vm)
    '''
    d = {}
    kmwfs = get_kmwfs(km)
    vmwfs = elel.get_wfs(vm)
    lngth = vmwfs.__len__()
    for i in range(0,lngth):
        value = elel._getitem_via_pathlist(vm,vmwfs[i])
        cond = elel.is_leaf(value)
        if(cond):
            _setitem_via_pathlist(d,kmwfs[i],value)
        else:
            _setdefault_via_pathlist(d,kmwfs[i])
    return(d)


def kmdfs_cond_func(ele,d,from_lv,to_lv,leaf_only,non_leaf_only):
    cond1 = (ele.__len__() >= from_lv)
    cond2 = (ele.__len__() <= to_lv)
    value = _getitem_via_pathlist(d,ele)
    leaf = is_leaf(value)
    if(leaf_only):
        cond3 = (leaf == True)
    elif(non_leaf_only):
        cond3 = (leaf == False)
    else:
        cond3 = True
    cond = (cond1 & cond2 & cond3)
    return(cond)



def _get_rvwfs(d):
    kmwfs = get_kmwfs(km)
    rvwfs = elel.array_map(kmwfs,getitem_via_pathlist,d)
    return(rvwfs)

def _get_rvdfs(d):
    km,vm = _d2kvmatrix(d)
    vmwfs = elel.get_wfs(vm)
    kmdfs = get_kmdfs(km,vmwfs)
    rvdfs = elel.array_map(kmdfs,getitem_via_pathlist,d)
    return(rvdfs)


def _get_rvmat(d):
    '''
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
                      'y3': 'v3'
                     }
              },
         't': 20,
         'u':
              {
               'u1': 'u2'
              }
        }
        
        
    '''
    km,vm = _d2kvmatrix(d)
    def map_func(ele,indexc,indexr):
        return(getitem_via_pathlist(d,ele))
    rvmat = elel.matrix_map(km,map_func)
    return(rvmat)




#######################

#refer to elist APIs for next development 



######################

class Edict():
    '''
        ed =Edict(bigd)
    '''
    def __init__(self,*args,**kwargs):
        '''
            ed =Edict(bigd)
        '''
        lngth = args.__len__()
        if(lngth == 1):
            self.dict = args[0]
        else:
            kl = args[0]
            vl = args[1]
            self.dict = kvlist2d(kl,vl)
    def klist(self):
        '''
            
        '''
        kl,vl = d2kvlist(self.dict)
        return(kl)
    def vlist(self):
        kl,vl = d2kvlist(self.dict)
        return(vl)
    def kvlists(self):
        return(d2kvlist(self.dict))
    def ktree(self):
        tr,nest = _d2kvmatrix(self.dict)
        return(tr)
    def vnest(self):
        tr,nest = _d2kvmatrix(self.dict)
        return(nest)
    def ktree_vnest(self):
        return(_d2kvmatrix(self.dict))
    def kwfs(self):
        tr,nest = _d2kvmatrix(self.dict)
        rslt = get_kmwfs(tr)
        return(rslt)
    def vwfs(self):
        tr,nest = _d2kvmatrix(self.dict)
        rslt = elel.get_wfs(nest)
        return(rslt)
    def rvwfs(self):
        return(_get_rvwfs(self.dict))
    def wfses(self):
        return(_d2kvmatrix(self.dict))
    def kdfs(self):
        tr,nest = _d2kvmatrix(self.dict)
        vwfs1 = elel.get_wfs(nest)
        rslt = get_kmdfs(tr,vwfs1)
        return(rslt)
    def vdfs(self):
        tr,nest = _d2kvmatrix(self.dict)
        vwfs1 = elel.get_wfs(nest)
        rslt = elel.wfs2dfs(vwfs1)
        return(rslt)
    def rvdfs(self):
        return(_get_rvdfs(self.dict))
    def dfses(self):
        return((self.kdfs(),self.vdfs()))
    def kdescmat(self):
        kdescm,vdescm = _scan(self.dict)
        return(kdescm)
    def vdescmat(self):
        kdescm,vdescm = _scan(self.dict)
        return(vdescm)
    def kvdescmats(self):
        return(_scan(self.dict))
    def include_pathlist(self,*args,**kwargs):
        cond = _include_pathlist(self.dict,list(args),**kwargs)
        return(cond)
    def pathlists(self):
        tr = self.ktree()
        pls = show_kmatrix(tr)
        return(pls)
    def bracket_lists(self):
        tr = self.ktree()
        brls = show_kmatrix_as_getStr(tr)
        return(brls)
    def __repr__(self):
        tr = self.ktree()
        show_kmatrix_as_getStr(tr)
        return(self.dict.__repr__())
    def __str__(self):
        return(self.dict.__str__())
    def __getitem__(self,*args,**kwargs):
        #very special in __getitem__
        if(isinstance(args[0],tuple)):
            #very special in __getitem__
            pl = list(args[0])
        else:
            #very special in __getitem__
            pl = list(args)
        return(_getitem_via_pathlist(self.dict,pl))
    def cond_select_via_key(self,cond_match=None,**kwargs):
        return(_cond_select_via_key(self.dict,cond_match=None,**kwargs))
    def cond_select_via_value(self,cond_match=None,**kwargs):
        return(_cond_select_via_value(self.dict,cond_match=None,**kwargs))
    def __setitem__(self,*args,**kwargs):
        #very special in __setitem__
        if(isinstance(args[0],tuple)):
            #very special in __getitem__
            pl = list(args[0])
            value = args[1]
        else:
            #very special in __getitem__
            pl = [args[0]]
            value = args[1]
        return(_setitem_via_pathlist(self.dict,pl,value))
    def setdefault(self,*args,**kwargs):
        '''
        '''
        return(_setdefault_via_pathlist(self.dict,list(args)))
    def __delitem__(self,*args,**kwargs):
        #very special in __getitem__
        if(isinstance(args[0],tuple)):
            #very special in __getitem__
            pl = list(args[0])
        else:
            #very special in __getitem__
            pl = list(args)
        return(_delitem_via_pathlist(self.dict,pl))
    def keys_via_value(self,value):
        return(_keys_via_value(self.dict,value))
    def vksdesc(self):
        return(_vksdesc(self.dict))
    def tree(self,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        if('show' in kwargs):
            show = kwargs['show']
        else:
            show = True
        kmdfs = self.kdfs()
        tr = elel.filter(kmdfs,kmdfs_cond_func,self.dict,from_lv,to_lv,leaf_only,non_leaf_only)
        if(show):
            elel.forEach(tr,print)
        else:
            pass
        return(tr)
    #@@@@@@@@
    #@@@@@@@@@@@
    def tlist(self):
        return(dict2tlist(self.dict))
    def mirrable(self):
        return(is_mirrable(self.dict))
    def mirror(self,**kwargs):
        md = dict_mirror(self.dict,**kwargs)
        return(md)
    def union(self,ed2,**kwargs):
        d3 = _union(self.dict,ed2.dict)
        return(Edict(d3))
    def diff(self,ed2,**kwargs):
        d3 = _diff(self.dict,ed2.dict)
        return(Edict(d3))
    def intersection(self,ed2,**kwargs):
        d3 = _intersection(self.dict,ed2.dict)
        return(Edict(d3))
    def complement(self,ed2,**kwargs):
        d3 = _complement(self.dict,ed2.dict)
        return(Edict(d3))
    def uniqualize(self,**kwargs):
        if('deepcopy' in kwargs):
            deepcopy = kwargs['deepcopy']
        else:
            deepcopy = 0
        d3 = _uniqualize(self.dict)
        if(deepcopy):
            pass
        else:
            self.dict = d3
        return(Edict(d3))
    def extend(self,ed2,**kwargs):
        if('deepcopy' in kwargs):
            deepcopy = kwargs['deepcopy']
        else:
            deepcopy = 0
        d3 = _extend(self.dict,ed2.dict,**kwargs)
        if(deepcopy):
            pass
        else:
            self.dict = d3
        return(Edict(d3))
    def comprise(self,ed2,**kwargs):
        cond = _comprise(self.dict,ed2.dict)
        return(cond)
    def update_intersection(self,ed2,**kwargs):
        if('deepcopy' in kwargs):
            deepcopy = kwargs['deepcopy']
        else:
            deepcopy = 0
        d3 = _update_intersection(self.dict,ed2.dict,**kwargs)
        if(deepcopy):
            pass
        else:
            self.dict = d3
        return(Edict(d3))
    def update(self,ed2,**kwargs):
        if('deepcopy' in kwargs):
            deepcopy = kwargs['deepcopy']
        else:
            deepcopy = 0
        d3 = _update(self.dict,ed2.dict,**kwargs)
        if(deepcopy):
            pass
        else:
            self.dict = d3
        return(Edict(d3))
    #################################
    #################################
    
#ktree 
#vnest 



#


def get_matloc_mapping(ktree,vdmat,attrname):
    kvm = {}
    vkm = {}
    for i in range(0,ktree.__len__()):
        klevel = ktree[i]
        vlevel = vdmat[i+1]
        for j in range(0,klevel.__len__()):
            k = tuple(klevel[j])
            v = tuple(vlevel[j][attrname])
            kvm[k] = v
            vkm[v] = k
    return((kvm,vkm))

def get_ktree_loc(ktree,kpath):
    lngth = kpath.__len__()
    level = lngth - 1
    klevel = ktree[level]
    index = klevel.index(kpath)
    return((level,index))

def ktrloc2vdloc(loc):
    return((loc[0]+1,loc[1]))

def vdloc2ktrloc(loc):
    return((loc[0]-1,loc[1]))

def get_attr_via_kpath_from_vdmat(vdmat,attrname,ktree,kpath):
    loc = get_ktree_loc(ktree,kpath)
    loc = ktrloc2vdloc(loc)
    return(vdmat[loc[0]][loc[1]][attrname])


#for checking 

class DictTree():
    '''
        dtree = DictTree(bigd)
    '''
    def __init__(self,*args,**kwargs):
        lngth = args.__len__()
        if(lngth == 1):
            self.dict = args[0]
            self.klist,self.vlist = d2kvlist(self.dict)
        else:
            self.klist = args[0]
            self.vlist = args[1]
            self.dict = kvlist2d(self.klist,self.vlist)
        self.ktree,self.vnest = _d2kvmatrix(self.dict)
        self.kwfs = get_kmwfs(self.ktree)
        self.vwfs = elel.get_wfs(self.vnest)
        self.kdfs = get_kmdfs(self.ktree,self.vwfs)
        self.vdfs = elel.wfs2dfs(self.vwfs)
        self.depth = self.ktree.__len__()
        self.kdescmat,self.vdescmat = _scan(self.dict)
    def __repr__(self):
        show_kmatrix_as_getStr(self.ktree)
        return(self.dict.__repr__())
    def tree(self,**kwargs):
        if('leaf_only' in kwargs):
            leaf_only = kwargs['leaf_only']
        else:
            leaf_only = False
        if('non_leaf_only' in kwargs):
            non_leaf_only = kwargs['non_leaf_only']
        else:
            non_leaf_only = False
        if('from_lv' in kwargs):
            from_lv = kwargs['from_lv']
        else:
            from_lv = 1
        if('to_lv' in kwargs):
            to_lv = kwargs['to_lv']
        else:
            to_lv = self.depth
        if('show' in kwargs):
            show = kwargs['show']
        else:
            show = True
        tr = elel.filter(kmdfs,kmdfs_cond_func,self.dict,from_lv,to_lv,leaf_only,non_leaf_only)
        if(show):
            elel.forEach(tr,print)
        else:
            pass
        return(tr)
    ####








