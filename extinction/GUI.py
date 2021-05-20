import tkinter as tk
import GUIfunc as guf
from tkinter import ttk


mwin = guf.Window()
s = ttk.Style()
print(s.theme_names())
s.theme_use('winnative')

grid_rc = [[50,40,40,40,40,40,40,40,40,40,40,40,40,40,40],[30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30,30]]
guf.configure_grid(mwin,grid_rc)

guf.create_widgets(mwin,tk)

mwin.mainloop()

c1,c2,c4,c5,x0,c3,gamma,O3,O2,O1,k_IR,R_V,ir_shrtst,opt_shrtst,uvN_shrtst,createoutput,scatter,fullplot = mwin.getvar(name="user_c1"),mwin.getvar(name="user_c2"),mwin.getvar(name="user_c4"),mwin.getvar(name="user_c5"),mwin.getvar(name="user_x0"),mwin.getvar(name="user_c3"),mwin.getvar(name="user_gamma"),mwin.getvar(name="user_O3"),mwin.getvar(name="user_O2"),mwin.getvar(name="user_O1"),mwin.getvar(name="user_k_IR"),mwin.getvar(name="user_R_V"),mwin.getvar(name="user_ir_shrtst"),mwin.getvar(name="user_opt_shrtst"),mwin.getvar(name="user_uvN_shrtst"),mwin.getvar(name="user_createoutput"),mwin.getvar(name="user_scatter"),mwin.getvar(name="user_fullplot")

