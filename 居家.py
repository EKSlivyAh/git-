'''
····················
居家项目
····················
编码·UTF-8
语言·Python 3.9.7 Linux,Python 3.10.9 Windows
依赖库·time,sys,os,rich
控制台颜色配置·黑底白字
版本·完整版
'''

# ····················库安装器
import sys, os
from time import sleep as s

try:
    from rich import print as cp
except ModuleNotFoundError:
    os.system('pip install rich')
    from rich import print as cp

# ····················初始化
p = print
day = '1'
C = '4'
light = '开'
mail = '最近没有'


# ····················类与函数
class tool:  # 工具箱
    def cls():  # 清屏
        p('\033[2J')
        p('\033[1;1H', end='')

    def dp(string):  # 逐字打印，普通p
        for char in list(string):
            print(char, end='', flush=True)
            s(0.05)


class pack:  # 游戏组件
    def wait():  # 开场启动
        p('\033[?25l', end='')
        cp('[cyan]Start cold boot...')
        p()
        p('Load BIOS...')
        s(0.2)
        p('Load kernel...')
        s(2)
        cp("[yellow]WANGING:You must have your own imagination about the fact that nuclear reactors can't avoid secondary barbecue, otherwise, print the function.")
        p('Load desktop...')
        s(2)

    def start():  # 主页
        cp('[black on cyan]慧家智能家庭中枢')
        tool.dp('你可以在慧家智能家庭中枢中轻松管理你的家庭，只需要输入代码，即可管理所有智能家电！')
        p('\033[?25h')
        p()
        cp('[yellow]new [/yellow]创建家庭')
        cp('[yellow]join [/yellow]加入家庭')
        cp('[yellow]about [/yellow]关于慧家')
        p()

    def about():  # 关于
        p('\033[?25l', end='')
        cp('[black on cyan]慧家智能家庭中枢')
        p('序列号:ssss.ssss.ssss.ssss')
        p('版本:1.2.2')
        p()

    def menu():  # 面板
        cp('[black on cyan]第' + day + '天     家庭名称:新的家庭')
        p('室内温度:' + C + '°C')
        p('灯:' + light)
        p('邮件:' + mail)
        p()
        cp('[yellow]light [/yellow]灯开关')
        cp('[yellow]mall [/yellow]查看邮件')
        cp('[yellow]con [/yellow]下一天')
        cp('[yellow]exit [/yellow]退出')
        p()

    def d1_d2():  # 第一天到第二天中间
        p('\033[?25l', end='')
        cp('[black on cyan]12月27日')
        tool.dp('我已经困在家一个月了。现在信号依然只能进不能出，门还是锁着的。虽然这几天灵异事件少了一点，但灯还是不能关。\n')
        tool.dp('等以后自由了，我就把这个房间送给其他新来的吧。\n')
        p()
        input('按回车键继续...')

    def mail_1():  # 邮件1
        p('\033[?25l', end='')
        cp('[black on cyan]发信人:isu')
        tool.dp('我是你的邻居，你家每天晚上都会传来奇怪的声音，有时还有尖叫和野兽嘶吼声，你的房门也打不开，已经严重影响到我们的生活作息。\n')
        tool.dp('你还好吗？我担心你，但是如果这些声音还在，我就会报警处理。\n')
        p()
        input('按回车键继续...')

    def d2_d3():  # 第二天到第三天中间
        p('\033[?25l', end='')
        cp('[black on cyan]12月28日')
        tool.dp('今天灯突然自己关闭了，明明没有问题啊。而且我已经不想呆在这个鬼地方了，现在能活过一天是一天吧。\n')
        p()
        input('按回车键继续...')

    def mail_2():  # 邮件2
        p('\033[?25l', end='')
        cp('[black on cyan]发信人:┼┏┏┘─││')
        tool.dp('║╕┛┡┥┯┲╡╲╓┤┳╙┸╃╆┢┥┵┈┹╞╕┳┫╇╟┺╆╀╋┬┗╒╲╲┅┇╛┒┒┖┦┦┮┝┝\n')
        tool.dp('┦┱╒┒┒┓┫┣┼╔╠╩╣╋┲┩┩┸┧║┿╀║╒┎┍┙╖┄┨╇╃┋┉┰╟\n')
        p()
        input('按回车键继续...')


# ····················游戏
if __name__ == '__main__':
    tool.cls()
    pack.wait()
    tool.cls()
    pack.start()
    while True:
        select = input('~~>')
        if select == 'new':
            tool.cls()
            input('IP地址·')
            p('\033[?25l', end='')
            cp('[on red]!错误[/on red]IP地址无效')
            input('按回车键返回...')
            tool.cls()
            pack.start()
        elif select == 'join':
            tool.cls()
            IP = input('IP地址·')
            port = input('端口·')
            password = input('密码·')
            agency = input('代理·')
            if IP == '592.169.75.294' and port == '7700' and password == 'As6IY6lh71v0oi632bnCdjD0a' and agency == '无':
                tool.cls()
                pack.menu()
                while True:
                    select = input('~~>')
                    if select == '':
                        pass
                    elif select == 'exit':
                        tool.cls()
                        p('\033[?25l', end='')
                        tool.dp('你觉得已经失去了希望，你退出了家庭，然后饮水自尽。\n')
                        p()
                        cp('[red]结局一·退出')
                        sys.exit(0)
                    elif select == 'light':
                        if day == '1':
                            tool.cls()
                            p('\033[?25l', end='')
                            tool.dp('你关掉了房子里唯一的灯，等等，那是什么？\n')
                            p()
                            cp('[red]结局二·那是什么')
                            sys.exit(0)
                        elif day == '2':
                            light = '开'
                            tool.cls()
                            pack.menu()
                        else:
                            light = '关'
                            tool.cls()
                            pack.menu()
                    elif select == 'mall':
                        if day == '1':
                            cp('[on blue]i提示[/on blue]最近没有邮件')
                        elif day == '2':
                            tool.cls()
                            pack.mail_1()
                            p('\033[?25h', end='')
                            tool.cls()
                            pack.menu()
                        else:
                            tool.cls()
                            pack.mail_2()
                            p('\033[?25h', end='')
                            tool.cls()
                            pack.menu()
                    elif select == 'con':
                        if day == '1':
                            tool.cls()
                            pack.d1_d2()
                            p('\033[?25h', end='')
                            light = '关'
                            C = '2'
                            mail = '新邮件！[1]'
                            day = '2'
                            tool.cls()
                            pack.menu()
                        elif day == '2':
                            if light == '关':
                                tool.cls()
                                p('\033[?25l', end='')
                                tool.dp('你在黑暗中睡觉，但也许会有东西在盯着你。\n')
                                p()
                                cp('[red]结局三·永远沉睡')
                                sys.exit(0)
                            else:
                                tool.cls()
                                pack.d2_d3()
                                p('\033[?25h', end='')
                                light = '开'
                                C = '4'
                                mail = '新邮件！[2]'
                                day = '3'
                                tool.cls()
                                pack.menu()
                        else:
                            if light == '开':
                                tool.cls()
                                p('\033[?25l', end='')
                                tool.dp('"啪！"一声，房屋黑了，一个月之久没有交电费，你的房间早已停电。\n')
                                tool.dp('你活不下去了。\n')
                                p()
                                cp('[red]结局四·停电')
                                sys.exit(0)
                            else:
                                tool.cls()
                                p('\033[?25l', end='')
                                tool.dp('当你躲避这些东西时，门被撞开了，警察来了！你得救了！\n')
                                tool.dp('但是，对于那封乱码邮件，你却无法破解。\n')
                                p()
                                cp('[yellow]完·Pinpe制作')
                                sys.exit(0)
                    else:
                        cp('[on red]!错误[/on red]语法错误')
            else:
                p('\033[?25l', end='')
                cp('[on red]!错误[/on red]无法连接')
                input('按回车键返回...')
                tool.cls()
                pack.start()
        elif select == 'about':
            tool.cls()
            pack.about()
            input('按回车键返回...')
            tool.cls()
            pack.start()
        elif select == '':
            pass
        else:
            cp('[on red]!错误[/on red]语法错误')
