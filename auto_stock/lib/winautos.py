# -*- coding: gbk -*-



from auto_stock.lib.config  import VK_CODE
#from pywinauto import application
import win32clipboard as wc
from auto_stock.lib.pykeyboard import PyKeyboard
import win32gui, win32api, win32con 
import time



class Winauto(object):
   
    def __init__(self):
        self.k = PyKeyboard() #get pykeyboard        
        self.software= u'���Ϲ�Ʊ����ϵͳ5.0'
        self.hWndChildList=0
        self.para_hld=win32gui.FindWindow(None,self.software)
        if self.IsWindow():
            self.hWndChildList=self.demo_child_windows(self.para_hld) #get hld 
            attr=self.show_window_attr(self.para_hld)
            win32api.SetCursorPos([attr['post'][0],attr['post'][1]]) #Mover to post(x,y)
			
    '''
    �ж������Ƿ񼤻�
    '''    
    def IsWindow(self):
        print (self.para_hld)
        if self.para_hld>0:
           return True;
        else:
           return False;
           
    '''
    �����ö�
    '''
    def topWindow(self):
        self.Key_event(VK_CODE['ctrl'])
        win32gui.SetForegroundWindow(self.para_hld)  #show window
        
    '''
    ��������¼�
    '''
    def Key_event(self,key):
        win32api.keybd_event(key,0,0,0) #
        win32api.keybd_event(key,0,win32con.KEYEVENTF_KEYUP,0) #
    '''
    ldList:
    'post:?��|left, top, right, bottom  
    '''
    def GetHld(self,post):
        for hld in self.hWndChildList:
            left, top, right, bottom =win32gui.GetWindowRect(hld) #get hld post left top right bottom
            #if (post[0]==left) & (post[1]==top) & (post[2]==right) & (post[3]==right):
            if (post[0]==left) & (post[1]==top): #get hld by (x,y) left top
                 return hld
        return 0
    '''
    ͨ���ַ��ҵ�����
    '''
    def GetHldWord(self,word):
        for hld in self.hWndChildList:
            title = win32gui.GetWindowText(hld)
            try:
                title = title.encode('utf-8').decode('gbk')
            except Exception as e:
                import traceback
                #print('traceback.print_exc():', traceback.print_exc())
                #logger.info(e)

            #if title != '':
            #    title=title.encode('utf-8').decode('gbk')
            if title==word:
                 return hld
        return 0
    
    '''
    ��ȡ�����µ������Ӵ���
    '''
    def demo_child_windows(self,parent):  
        if not parent:  
            return   
        hWndChildList = []  
        win32gui.EnumChildWindows(parent, lambda hWnd, param: param.append(hWnd),  hWndChildList)  
        return hWndChildList  
    
	#get all hld attr
    def show_window_attr(self,hWnd):  
        if not hWnd:  
            return  
       
        title = win32gui.GetWindowText(hWnd)  
        clsname = win32gui.GetClassName(hWnd) 
        left, top, right, bottom =win32gui.GetWindowRect(hWnd) #
        attr = {'hWnd':hWnd,'title': title, 'clsname':clsname, 'post':[left,top,right,bottom]}    
    
        return attr

    '''
        �����Ʊ����
        

    def Buy(self, buy_stock, buy_price, buy_nun):
        self.topWindow()
        self.Key_event(VK_CODE['F2'])
        self.Key_event(VK_CODE['F1'])
        self.backspace(5)
        time.sleep(0.5)
        self.k.type_string(buy_stock)
        self.Key_event(VK_CODE['tab'])
        time.sleep(1)
        if buy_price != '0':
            self.k.type_string(buy_nun)
        self.Key_event(VK_CODE['tab'])
        self.k.type_string(buy_nun)
        time.sleep(1)
        self.Key_event(VK_CODE['enter'])
        time.sleep(1)
        self.Key_event(VK_CODE['enter'])
        time.sleep(1)
        self.Key_event(VK_CODE['enter'])
        time.sleep(1)
        self.Key_event(VK_CODE['enter'])'''


    '''
    �����Ʊ
    '''
    def Buy(self,buy_stock,buy_price,buy_nun):
        self.topWindow()
        self.Key_event(VK_CODE['F2'])
        self.Key_event(VK_CODE['F1'])
        self.backspace(5)
        time.sleep(0.1)
        self.k.type_string(buy_stock) 
        self.Key_event(VK_CODE['tab'])
        time.sleep(0.1)
        if buy_price!='0':        
            self.k.type_string(buy_nun) 
        self.Key_event(VK_CODE['tab'])
        self.k.type_string(buy_nun)
        #time.sleep(0.1)
        self.Key_event(VK_CODE['enter'])
        #time.sleep(0.1)
        self.Key_event(VK_CODE['enter'])
        #time.sleep(0.1)
        self.Key_event(VK_CODE['enter'])
        #time.sleep(0.1)
        self.Key_event(VK_CODE['enter'])
        
	
    def Sell(self,buy_stock,buy_price,buy_nun):
         self.topWindow()
         self.Key_event(VK_CODE['F1'])
         self.Key_event(VK_CODE['F2'])
         self.backspace(5)
         time.sleep(0.5)
         self.k.type_string(buy_stock)            
         self.Key_event(VK_CODE['tab'])
         time.sleep(1)                             
         if buy_price!='0':
             self.k.type_string(buy_price) 
         self.Key_event(VK_CODE['tab'])
         self.k.type_string(buy_nun) 
         self.Key_event(VK_CODE['enter'])
         self.Key_event(VK_CODE['enter']) 
       
    
    def getAllAsset(self):
        self.topWindow()
        time.sleep(0.5)#    
        win32api.keybd_event(VK_CODE['F4'],0,0,0)  #
        distance = 54 #left_distance
        balance      = u'�ʽ����'
        #ͨ�������ж�

        #import time as time2
        #start = time.time()
        balance = self.getSset(balance, distance)
        #stop = time.time()
        #print('delay: %.3fs' % (stop - start))

        othe_balance = u'���ý��'
        othe_balance =self.getSset(othe_balance,distance)
        market_value = u'��Ʊ��ֵ'
        market_value =self.getSset(market_value,distance)
        propertys    = u'�� �� ��'
        propertys =self.getSset(propertys,distance)
        AssetList={'balance':balance['title'],'othe_balance':othe_balance['title'],'market_value':market_value['title'],'propertys':propertys['title']}
        return AssetList
    
    def backspace(self,n):
        for i in range(0,n):     
           self.Key_event(VK_CODE['backspace'])
         
        
        
    def getSset(self,word,distance):
        hld  = self.GetHldWord(word) 
        attr     = self.show_window_attr(hld)
        hld  = self.GetHld((attr['post'][0]+distance,attr['post'][1]))
        attr     = self.show_window_attr(hld)
        return attr
        
	#start app go go go
    def appStart(self,fileext,ver):
        win32api.ShellExecute(0, 'open',fileext,ver,'',1)       
        time.sleep(5)
        self.k.type_string(self.password)
        win32api.keybd_event(VK_CODE['tab'],0,0,0) 
        win32api.keybd_event(VK_CODE['enter'],0,0,0)
    
    '''
    ctrl+c
    '''    
    def copyKey(self):
        win32api.keybd_event(VK_CODE['ctrl'],0,0,0)      # Alt
        win32api.keybd_event(VK_CODE['c'],0,0,0)        # O
        win32api.keybd_event(VK_CODE['c'],0,win32con.KEYEVENTF_KEYUP,0)  #
        win32api.keybd_event(VK_CODE['ctrl'],0,win32con.KEYEVENTF_KEYUP,0)		

    '''
    ��ȡ�ֲ�
    '''
    def getAllStock(self):
        win32api.keybd_event(VK_CODE['F4'],0,0,0)
        attr = self.show_window_attr(self.para_hld)
        x = attr['post'][0]+300
        y = attr['post'][1]+300
        win32api.SetCursorPos([x,y]) #Mover to post(x,y)
        self.copyKey()                                                
        copy_txt = self.getCopyText()          							
        copy_txt = copy_txt.rstrip().split("\n") 
        c = []
        cArray = {}
        cloun =  ''
        for vv in  copy_txt:
            cloun =  vv.split("	") 
            for v in cloun:        
                c.append(v)
            cArray[c[1]]=c       
            c=[]                   
        return cArray
		     
    '''
    ʵ�ָ��ƹ���
    '''            
    def getCopyText(self):
            wc.OpenClipboard()
            copy_text = wc.GetClipboardData(win32con.CF_TEXT)
            wc.CloseClipboard()
            return copy_text	

    '''
    �ر����
    '''
    def closApp(self):
        
          self.para_hld=win32gui.FindWindow(None,self.software) #get hld by app word
        
          win32gui.PostMessage(self.para_hld, win32con.WM_CLOSE, 0, 0)
       
#kk = Winauto()
#kk.topWindow()
#kk.Buy('002456','0','200')  
#k=kk.getAllAsset()
#print k
#writTxt('x.txt',str(len(k)))
#time.sleep(2)  
#kk.closApp()
#kk.SellS('600663','0','1000')



def main_buy(stock,price,nun):

    kk = Winauto()
    #AssetList=kk.getAllAsset()
    #AssetList=kk.getAllAsset()
	#AssetList=kk.getAllAsset()
    #print( AssetList)
    #value = AssetList['othe_balance']  #balance
    # price = price
    ##nun = int(value/(price*100))*100      #can buy stock nun
    import time
    start = time.time()
    kk.Buy(stock, '100', '100')
    stop = time.time()
    print('delay: %.3fs' % (stop - start))

    #kk.getAllAsset()
	# time.sleep(60)
	# kk.closApp()                      #close app
	
#main_buy('601288', 100, 100)

def main_SellS(stock,price,nun):

	kk = Winauto() ;time.sleep(2)
	AssetList=kk.getAllAsset()
	#value = AssetList['othe_balance']  #balance
	#price = price                         
	#nun = int(value/(price*100))*100      #can buy stock nun
   
	kk.SellS(stock,price,nun)
	time.sleep(10)
	kk.closApp()                      #close app
	

if __name__ == '__main__':
    main_buy('601288', 100, 100)


      
