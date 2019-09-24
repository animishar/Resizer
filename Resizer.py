import tkinter,cv2,glob,os
from tkinter import ttk,filedialog
global dir_
h=0
w=0

def task():
	global h,w
	width=w
	height=h
	try:
		os.mkdir(dir_+"Resized")
	except:
		print("Dir exists ")
	new_dir=(dir_+"/Resized/")
	jpg_files=glob.glob(dir_+"*.jpg")
	print(jpg_files,"->",dir_)
	total=len(jpg_files)
	prog=0
	lbl1.configure(text="	Processing")
	for jpg_file in jpg_files:
		prog+=1
		img=cv2.imread(jpg_file, cv2.IMREAD_UNCHANGED)
		print("image",type(img))
		title,ext=os.path.splitext(os.path.basename(jpg_file))
		H,W=img.shape[:2]
		pad_bottom, pad_right=0,0
		ratio=W/H
		if H>height or W>width:
			interp=cv2.INTER_AREA
		else:
			interp=cv2.INTER_CUBIC
		W=width
		H=round(w/ratio)
		if H>height:
			H=height
			W=round(h*ratio)
		pad_bottom=abs(height - H)
		pad_right=abs(width - W)
		scaled_img=cv2.resize(img, (W, H), interpolation=interp)
		padded_img=cv2.copyMakeBorder(scaled_img,0,pad_bottom,0,pad_right,borderType=cv2.BORDER_CONSTANT,value=[0,0,0]) 
		cv2.imwrite(new_dir+title+ext, padded_img)
		val=prog/total
		val*=100
		string='	Processing '+str(int(val))+'%  done'
		lbl1.configure(text=string)
		print(int(val))
		progress['value']=int(val)
		root.update_idletasks()
	lbl1.configure(text="	 Done :)		")
	close.configure(state="normal")
	step_lbl.configure(text="Resizing complete \n made by: Animisha ")
	start.configure(state="disable")
def browser():
	global dir_
	dir_=filedialog.askdirectory()+"/"
	hidden.configure(text=dir_)
	print (dir_)
def callback():
	global dir_
	if len(glob.glob(dir_+"*.jpg"))==0:
		temp=tkinter.Tk()
		temp.title("Warning")
		tlab=tkinter.Label(temp,text="No images found in the directory!! ")
		tbtn=tkinter.Button(temp,text="Close",command=temp.destroy)
		tlab.pack()
		tbtn.pack()

	else:  
		browse.configure(state="disabled")
		ent.configure(state="disabled")
		lbl.configure(state="disabled",text="loaded images")
		load.configure(state="disabled")
		step_lbl.configure(text="step 2/3")

		wlbl.configure(state="normal")
		hlbl.configure(state="normal")
		width_.configure(state="normal")
		height_.configure(state="normal")
		btn.configure(state="normal")
		lbl2.configure(state="normal")
		
def callback2():
	width,height=width_.get(),height_.get()
	global w,h
	try:
		w,h=float(width),float(height)
		w,h=int(w),int(h)
		wlbl.configure(state="disabled")
		hlbl.configure(state="disabled")
		width_.configure(state="disabled")
		height_.configure(state="disabled")
		btn.configure(state="disabled")
		lbl2.configure(state="disabled",text=":)")

		lbl1.configure(state="normal")
		start.configure(state="normal")
		step_lbl.configure(text="step 3/3")

	except:
		lbl2.configure(text="Enter proper dimensions")
		temp=tkinter.Tk()
		temp.title("Warning")
		tlab=tkinter.Label(temp,text="Enter Proper dimensions ")
		tbtn=tkinter.Button(temp,text="Close",command=temp.destroy)
		tlab.pack()
		tbtn.pack()
		w,h=0,0

root=tkinter.Tk()
root.title("Resizer")

frame1=tkinter.Frame(root)
frame2=tkinter.Frame(root)
frame3=tkinter.Frame(root)

log_label=tkinter.Label(root,text="RESIZER TOOL",font=("Helvetica",16))

step_lbl=tkinter.Label(root,text="step 1/3",font="Arial")
lbl=tkinter.Label(frame1,text="Enter dir ")
ent=tkinter.Entry(frame1)
browse=tkinter.Button(frame1,text="Browse",command=browser)
hidden=tkinter.Label(frame1,text="        click->")
load=tkinter.Button(frame1,text="Load",command=callback)

wlbl=tkinter.Label(frame2,text="Width",state="disabled")
lbl2=tkinter.Label(frame2,text="Set dimensions",state='disabled')
hlbl=tkinter.Label(frame2,text="Height",state="disabled")
height_=tkinter.Entry(frame2,width=10,state="disabled")
width_=tkinter.Entry(frame2,width=10,state="disabled")
btn=tkinter.Button(frame2,text="next",state='disabled',command=callback2)

lbl1=tkinter.Label(frame3,text="  Press start to initiate.  ",state='disabled')
start=tkinter.Button(frame3,text="Start",state='disabled',command=task)
close=tkinter.Button(frame3,text="Finish",command=root.destroy,state="disabled")
progress=ttk.Progressbar(frame3,orient=tkinter.HORIZONTAL,length=100,mode='determinate')

log_label.grid(row=0,columnspan=3)

lbl.grid(row=1,column=0,)
hidden.grid(row=1,column=1)
#ent.grid(row=1,column=1)
browse.grid(row=1,column=2)
load.grid(row=2,columnspan=2)
frame1.grid(row=1,column=0)

lbl2.grid(row=0,columnspan=2)
wlbl.grid(row=1,column=0)
width_.grid(row=1,column=1)
hlbl.grid(row=2,column=0)
height_.grid(row=2,column=1)
btn.grid(row=3,columnspan=2)
frame2.grid(row=1,column=2)

lbl1.grid(row=0,column=0)
start.grid(row=1,column=0)
progress.grid(row=2,column=0)
close.grid(row=3,column=0)
frame3.grid(row=1,column=4)

step_lbl.grid(row=2,columnspan=4)

root.mainloop()