class Settings:
    '''存储游戏《外星人入侵》中的所有设置类'''

    def __init__(self):
        '''初始化游戏的设置'''
        # 屏幕保护
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船设置
        self.ship_speed = 1.5
        self.ship_limit = 3

        #子弹设置
        self.bullet_speed = 1.5
        self.bullet_width = 15
        self.bullet_height = 3
        # 子弹颜色
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 10 # 限制最大子弹数
        # 外星人设置
        self.alien_speed = 1.0 # 速度
        self.fleet_drop_speed = 10

        # 加快游戏节奏的速度
        self.speedup_scale = 1.2
        # 外星人分数的提高速度
        self.score_scale = 1.5

        # 初始化游戏动态设置
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """初始化随游戏进行而变化的设置"""
        self.ship_speed = 1.5
        self.bullet_speed = 3.0
        self.alien_speed = 1.0

        # fleet_direction 为1表示向右移， 为-1表示向左移
        # fleet_direction 为1表示向下移， 为-1表示向上移
        self.fleet_direction = 1

        # 计分
        self.alien_points = 50

    def increase_speed(self):
        """提高速度设置"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        """提高速度设置和外星人分数"""
        self.alien_points = int(self.alien_points * self.score_scale)



