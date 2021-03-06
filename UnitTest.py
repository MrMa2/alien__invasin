import unittest
from unittest import TestCase
from pymouse import PyMouse
import win32api
import win32con
from unittest.mock import Mock
from alien_invasion import AlienInvasion


class UpDownTest(TestCase):
    """单元测试的类."""

    def test_up(self):
        """测试飞船按上方向键"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        # 按上键
        win32api.keybd_event(38, 0, 0, 0)

        for i in range(1000):
            mock_obj._check_events()
            mock_obj.ship.update()

        # 按上键后moving_up是否变为True
        self.assertEqual(mock_obj.ship.moving_up, True)
        # 按上键后飞船是否超过边界
        self.assertEqual(mock_obj.ship.rect.y, 0)

        # 松开上键
        win32api.keybd_event(38, 0, win32con.KEYEVENTF_KEYUP, 0)
        mock_obj._check_events()
        mock_obj.ship.update()
        # 松开上键后moving_up是否变为False
        self.assertEqual(mock_obj.ship.moving_up, False)

    def test_down(self):
        """按下方向键测试"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()
        # 按下键
        win32api.keybd_event(40, 0, 0, 0)

        for i in range(1000):
            mock_obj._check_events()
            mock_obj.ship.update()
        # 按下键后moving_down是否变为True
        self.assertEqual(mock_obj.ship.moving_down, True)
        # 按下键后飞船是否超过边界
        self.assertEqual(mock_obj.ship.rect.bottom, mock_obj.screen.get_rect().bottom)

        # 松开下键
        win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)
        mock_obj._check_events()
        mock_obj.ship.update()
        # 松开下键后moving_down是否变为False
        self.assertEqual(mock_obj.ship.moving_down, False)

    def test_left(self):
        """按左方向键测试"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        # 按左方向键
        win32api.keybd_event(37, 0, 0, 0)

        for i in range(1000):
            mock_obj._check_events()
            mock_obj.ship.update()
        # 按左键后moving_left是否变为True
        self.assertEqual(mock_obj.ship.moving_left, True)
        # 按左键后飞船是否超过边界
        self.assertEqual(mock_obj.ship.rect.left, mock_obj.screen.get_rect().left)

        # 松开左键
        win32api.keybd_event(37, 0, win32con.KEYEVENTF_KEYUP, 0)
        mock_obj._check_events()
        mock_obj.ship.update()
        # 松开左键后moving_left是否变为False
        self.assertEqual(mock_obj.ship.moving_left, False)

    def test_right(self):
        """按右方向键测试"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        # 按右方向键
        win32api.keybd_event(39, 0, 0, 0)

        for i in range(1000):
            mock_obj._check_events()
            mock_obj.ship.update()
        # 按右键后moving_right是否变为True
        self.assertEqual(mock_obj.ship.moving_right, True)

        # 松开右键
        win32api.keybd_event(39, 0, win32con.KEYEVENTF_KEYUP, 0)
        mock_obj._check_events()
        mock_obj.ship.update()
        # 松开右键后moving_right是否变为False
        self.assertEqual(mock_obj.ship.moving_right, False)

    def test_space(self):
        """按空格键测试"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()
        """按空格键"""
        # 第二个参数为空格按下的硬件扫描码
        win32api.keybd_event(32, 0x39, 0, 0)
        mock_obj._check_events()
        # 按向下空格键后子弹是否产生
        self.assertEqual(len(mock_obj.bullets), 1)

    def test_click(self):
        """鼠标左键测试"""
        ai = AlienInvasion()
        mock_g = Mock(return_value=ai)
        mock_obj = mock_g()

        # 初始值
        self.assertEqual(mock_obj.stats.game_active, False)
        """点击鼠标"""
        m = PyMouse()
        # 点击位置
        m.click(mock_obj.play_button.rect.x, mock_obj.play_button.rect.y)
        mock_obj._check_events()
        # 鼠标点击是否成功
        self.assertEqual(mock_obj.stats.game_active, True)


if __name__ == '__main__':
    unittest.main()