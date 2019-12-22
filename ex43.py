from sys import exit
from random import randint
from textwrap import dedent


class Scene(object):

    def enter(self):
        print("This scene is not yet configured.")
        print("Subclass it and implement enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map
    
    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')
        
        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

class Death(Scene):
    
    quips = [
        "你挂了。玩得真烂。",
        "你妈一定自豪极了……有你这么个倒霉孩子。",
        "逊爆了。",
        "我家小狗都玩得比你好。",
        "你比你爸讲的笑话还烂。"
    ]
    
    def enter(self):
        print(Death.quips[randint(0, len(Death.quips)-1)])
        exit(1)


class CentralCorridor(Scene):

    def enter(self):
        print(dedent("""
            来自行星 Percal #25 的 Gothon 外星人入侵了你的飞船并杀死了你所有的船员，你是唯一的幸存者。你的任务是从【军火库】拿到【中子爆裂弹】，把它安置在【桥】上，然后在进入【逃生舱】之前将其引爆。
            
            你正沿着【中央走廊】向【军火库】跑去，这时一个 Gothon 跳了出来，它浑身布满红色鳞片，长有又黑又脏的牙齿，邪恶的小丑服飞舞着包裹住充斥着仇恨的躯体。它堵在通往【军火库】的门前，拿着激光枪准备攻击你。
            """))
        print(dedent("""
            1. 开枪！
            2. 闪避！
            3. 讲个笑话
            """))
        action = input("> ")
        
        if action == "1":
            print(dedent("""
                说时迟那时快，你抽出了激光枪射向 Gothon。然而激光全打在了它那飞舞着的小丑服上，一发也没射中它的身体。你把这件衣服打坏了，这是它妈咪给它买的，还是新的呢。它陷入了狂怒状态，朝你脸上反复开枪，然后它吃了你。
                """))
            return 'death'
        
        elif action == "2":
            print(dedent("""
                就在 Gothon 朝你头部射击的瞬间，你像个世界级拳击手一样闪躲、穿梭、滑行。在那充满艺术感的躲避过程中，你脚滑了，头撞在金属质地的墙上，眼冒金星。你刚回过神来，Gothon 就踩扁你的头，吃了你。
                """))
            return 'death'
            
        elif action == "3":
            print(dedent("""
                真庆幸念书的时候学了怎么用 Gothon 语说脏话。你给它讲你听过的一个笑话：哔哩吧啦吧啦卟，吧啦哔哩哔哩噗，噶叽噶叽酷酷酷！Gothon 停下了动作，死命忍住笑，却笑抽了。趁着它笑，你朝它跑去，一枪崩了它的脑袋，把它放倒，然后进入【军火库】。
                """))
            return 'laser_weapon_armory'
        
        else:
            print("请输入一个数字选项！")
            return 'central_corridor'


class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            你一头扎进【军火库】，蹲下来扫视四周有没有潜伏着的 Gothon。真安静，连根针掉在地上都能听见。你站起来向对面跑去，找到了装在盒子中的【中子爆裂弹】。盒子上着锁，需要输入密码。如果10次都输入了错误的密码，盒子将被永远锁住，你就拿不到【中子爆裂弹】了。密码是三位数字。
            """))
        
        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        chances = 10
        guess = ""
        
        while guess not in ["000", code] and chances > 0:
            guess = input(f"你还有{chances}次机会。密码键盘> ")
            if guess not in ["000", code]:
                print("× 密码错误 ×\n")
            chances -= 1
            
        if guess in ["000", code]:
            print("√ 密码正确 √")
            print(dedent("""
                盒子打开了。你取出【中子爆裂弹】，以最快的速度冲向炸弹的安置地点：【桥】。
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                密码锁发出最后一声错误提示后，你听到了那令人不快的机械熔化并焊接在一块儿的声音。你决定躲在这里，最后 Gothon 从它们的飞船往这里开炮，你死了。
                """))
            return 'death'


class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            你冲上了【桥】，胳膊底下夹着【中子爆裂弹】，惊动了5个试图控制这艘飞船的 Gothon。它们各个都穿着比之前那位还丑的小丑服。它们没有开枪，因为不想引爆你拿着的，已经开始倒计时的炸弹。
            """))
        print(dedent("""
            1. 朝 Gothon 扔炸弹
            2. 缓缓安置炸弹
            """))
        action = input("> ")
        
        if action == "1":
            print(dedent("""
            你慌里慌张地将炸弹丢向 Gothon 们，并朝门的方向跃去。你一丢下炸弹，一个 Gothon 就朝你背部开枪了。你死前看到另一个 Gothon 疯了一般想要拆解炸弹，也许它们都会被炸死吧。
            """))
            return 'death'
        
        elif action == "2":
            print(dedent("""
            你用镭射枪指着怀里的炸弹，Gothon 们都举起手来，开始冒冷汗。你一步步挪向门，开门，小心地将炸弹安置在地上，仍用镭射枪指着它。然后你一跃过门，捶下关门按钮，把开锁装置一枪崩了，这样 Gothon 们就出不来了。炸弹已安置好，你朝【逃生舱】跑去。
            """))
            return 'escape_pod'
        
        else:
            print("请输入一个数字选项！")
            return 'the_bridge'


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            你在飞船中飞奔，急切地想要在飞船爆炸前进入【逃生舱】。飞船中似乎已经不剩什么 Gothon 了，所以你没遇到阻碍。你到达安放【逃生舱】的厅室，现在需要选一个进行逃生。其中一些可能是坏的，但你没有检查的时间了。有5个【逃生舱】，选哪个呢？
            """))
        good_pod = randint(1,5)
        guess = input("选择？号逃生舱> ")
        
        while guess not in ['0','1','2','3','4','5']:
            print("快选一个逃生舱！")
            guess = input("选择？号逃生舱> ")
        if int(guess) not in [0, good_pod]:
            print(dedent(f"""
                你进入【{guess}号逃生舱】并摁下发射按钮。【逃生舱】驶入太空，舱体爆裂，把你炸成了浆糊。
                """))
            return 'death'
        else:
            print(dedent(f"""
                你进入【{guess}号逃生舱】并摁下发射按钮。【逃生舱】顺利地驶入太空，飞向一颗行星。你转身望去，你逃离的飞船爆炸了，像颗耀眼的恒星，把 Gothon 的飞船也给炸了。你赢了！
                """))
            return 'finished'

class Finished(Scene):

    def enter(self):
        print("You won! Good job.")
        return 'finished'


class Map(object):
    
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished()
    }
    
    def __init__(self, start_scene):
        self.start_scene = start_scene
    
    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    
    def opening_scene(self):
        return self.next_scene(self.start_scene)


a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()