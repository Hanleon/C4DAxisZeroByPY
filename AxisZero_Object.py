import c4d

def main():
    # 选择要归零的坐标，都为False为物体中心
    isX = False
    isY = True
    isZ = False
    
    objs = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    if not objs:
        return

    for obj in objs:
        ps = obj.GetAllPoints()
        m = obj.GetMg()

        center = obj.GetMp()
        rad = obj.GetRad()
        print(isY)
        center -= c4d.Vector((rad.x if isX else 0),(rad.y if isY else 0),(rad.z if isZ else 0)) 
        
        center *= m 

        new_m = c4d.Matrix(m)
        new_m.off = center

        loc_m = ~new_m * m

        obj.SetAllPoints([loc_m.Mul(p) for p in ps])
        obj.SetMg(new_m)
        
        obj.Message(c4d.MSG_UPDATE)
    
    c4d.EventAdd()


if __name__ == '__main__':
    main()
