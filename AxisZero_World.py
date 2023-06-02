import c4d

def main():
    #最终移动坐标
    pos = c4d.Vector(0, 0, 0)
    
    objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not objs:
        return
    
    for obj in objs:
        ps = obj.GetAllPoints()
        m = obj.GetMg()
    
        center = obj.GetMp()
        rad = obj.GetRad()
        
        center -= c4d.Vector(0,rad.y,0)
        
        center *= m 
    
        new_m = c4d.Matrix(pos)
    
        loc_m = ~new_m * m
        
        obj.SetAllPoints([loc_m.Mul(p) for p in ps])
        obj.SetMg(new_m)
        obj.Message(c4d.MSG_UPDATE)
    
    c4d.EventAdd()

if __name__=='__main__':
    main()
