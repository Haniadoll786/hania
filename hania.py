import platform

bit=platform.architecture()[0]

if bit=="64bit":
    import hbig
    hbig.gf()
elif bit=="32bit":
    import fire
    fire.main()
