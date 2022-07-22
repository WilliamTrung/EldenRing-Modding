# -*- coding: utf-8 -*-
def t602006000_1():
    """State 0,1"""
    t602006000_x0()
    Quit()

def t602006000_x0():
    """State 0"""
    if not IsClientPlayer():
        """State 1"""
        Label('L0')
        call = t602006000_x1()
        if IsClientPlayer() == 1:
            """State 2"""
            Label('L1')
            call = t602006000_x2()
            if not IsClientPlayer():
                Goto('L0')
            elif IsPlayerDead() == 1:
                pass
        elif IsPlayerDead() == 1:
            pass
    else:
        Goto('L1')
    """State 3"""
    call = t602006000_x4()
    assert not IsPlayerDead()
    Goto('L0')
    """Unused"""
    """State 4"""
    return 0

def t602006000_x1():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6250:"Use smithing table"
        call = t602006000_x5(actionbutton1=6250, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                             flag6=6000)
        if call.Done():
            """State 2"""
            call = t602006000_x3()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 3 or IsMultiplayerInProgress() == 1:
                pass
        elif IsMultiplayerInProgress() == 1:
            pass
        """State 3"""
        assert t602006000_x6() and not IsMultiplayerInProgress()
    """Unused"""
    """State 4"""
    return 0

def t602006000_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t602006000_x3():
    """State 0"""
    while True:
        """State 1"""
        Label('L0')
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:26020000:"Strengthen armament"
        AddTalkListData(1, 26020000, -1)
        # action:26020000:"Use Whetblade Fragment"
        AddTalkListData(2, 26021000, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        if GetTalkListEntryResult() == 1:
            CombineMenuFlagAndEventFlag(6001, 232)
            CombineMenuFlagAndEventFlag(6001, 233)
            CombineMenuFlagAndEventFlag(6001, 234)
            CombineMenuFlagAndEventFlag(6001, 235)
            c1_141(9)
            OpenEnhanceShop(0)
            assert not (CheckSpecificPersonMenuIsOpen(9, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        elif GetTalkListEntryResult() == 2: #Whetb
            if ComparePlayerInventoryNumber(3, 8969, 2, 0, 0) == 1:
                if GetEventFlag(65610) == 0 or GetEventFlag(65620) == 0 or GetEventFlag(65630) == 0 or GetEventFlag(65640) == 0 or GetEventFlag(65650) == 0 or GetEventFlag(65660) == 0 or GetEventFlag(65670) == 0 or GetEventFlag(65680) == 0 or GetEventFlag(65690) == 0 or GetEventFlag(65700) == 0 or GetEventFlag(65710) == 0 or GetEventFlag(65720) == 0 or GetEventFlag(65730) == 0 or GetEventFlag(65740) == 0 or GetEventFlag(65750) == 0 or GetEventFlag(65760) == 0 or GetEventFlag(65770) == 0 or GetEventFlag(65780) == 0 or GetEventFlag(65790) == 0 or GetEventFlag(65800) == 0 or GetEventFlag(65810) == 0 or GetEventFlag(65820) == 0:   
                    assert t602006000_x10()
                else:
                    call = t602006000_x9(action1=26021002)
                    if call.Done():
                        Goto('L0')
            else:
                call = t602006000_x9(action1=26021001)
                if call.Done():
                    Goto('L0')
        else:
            """State 6,11"""
            return 0
    """Unused"""
    """State 7,10"""
    OpenEquipmentChangeOfPurposeShop()
    assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    Goto('L0')

def t602006000_x4():
    """State 0,2"""
    assert t602006000_x6()
    """State 1"""
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t602006000_x5(actionbutton1=6250, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag1) == 1 or GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1 or GetEventFlag(flag4)
                == 1 or GetEventFlag(flag5) == 1)
        """State 4"""
        assert not GetEventFlag(flag6)
        """State 2"""
        if GetEventFlag(flag6) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag1) and not GetEventFlag(flag2) and not GetEventFlag(flag3) and not
              GetEventFlag(flag4) and not GetEventFlag(flag5)):
            pass
        # actionbutton:6250:"Use smithing table"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t602006000_x6():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t602006000_x8(action2=_):
    """State 0,1"""
    OpenGenericDialog(8, action2, 3, 4, 2)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    if GetGenericDialogButtonResult() == 1:
        """State 3"""
        return 0
    else:
        """State 4"""
        return 1

def t602006000_x9(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t602006000_x10():
    assert GetCurrentStateElapsedTime() > 0.1
    if ComparePlayerInventoryNumber(3, 8969, 2, 0, 0) == 0:
        return 0
    else:
        c1_110()
    while True:
        ClearTalkListData()
        if ComparePlayerInventoryNumber(3, 8969, 2, 0, 0) == 0:
            return 0
        else:
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65610) == 0, 10, 26021010, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65620) == 0, 20, 26021020, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65630) == 0, 30, 26021030, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65680) == 0, 40, 26021040, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65760) == 0, 50, 26021050, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65650) == 0, 60, 26021060, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65730) == 0, 70, 26021070, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65670) == 0, 80, 26021080, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65790) == 0, 90, 26021090, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65640) == 0, 100, 26021100, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65660) == 0, 110, 26021110, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65810) == 0, 120, 26021120, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65700) == 0, 130, 26021130, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65710) == 0, 140, 26021140, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65720) == 0, 150, 26021150, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65820) == 0, 160, 26021160, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65800) == 0, 170, 26021170, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65770) == 0, 180, 26021180, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65780) == 0, 190, 26021190, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65690) == 0, 200, 26021200, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65740) == 0, 210, 26021210, -1)
            # action:"Affinity"
            AddTalkListDataIf(GetEventFlag(65750) == 0, 220, 26021220, -1)
        # action:"Cancel"
        AddTalkListData(99, 15000460, -1)
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        if ComparePlayerInventoryNumber(3, 8969, 2, 0, 0) == 0:
            return 0
        elif GetTalkListEntryResult() == 10:
            assert t602006000_x11(aFlag=65610, aText=26021010)
        elif GetTalkListEntryResult() == 20:
            assert t602006000_x11(aFlag=65620, aText=26021020)
        elif GetTalkListEntryResult() == 30:
            assert t602006000_x11(aFlag=65630, aText=26021030)
        elif GetTalkListEntryResult() == 40:
            assert t602006000_x11(aFlag=65680, aText=26021040)
        elif GetTalkListEntryResult() == 50:
            assert t602006000_x11(aFlag=65760, aText=26021050)
        elif GetTalkListEntryResult() == 60:
            assert t602006000_x11(aFlag=65650, aText=26021060)
        elif GetTalkListEntryResult() == 70:
            assert t602006000_x11(aFlag=65730, aText=26021070)
        elif GetTalkListEntryResult() == 80:
            assert t602006000_x11(aFlag=65670, aText=26021080)
        elif GetTalkListEntryResult() == 90:
            assert t602006000_x11(aFlag=65790, aText=26021090)
        elif GetTalkListEntryResult() == 100:
            assert t602006000_x11(aFlag=65640, aText=26021100)
        elif GetTalkListEntryResult() == 110:
            assert t602006000_x11(aFlag=65660, aText=26021110)
        elif GetTalkListEntryResult() == 120:
            assert t602006000_x11(aFlag=65810, aText=26021120)
        elif GetTalkListEntryResult() == 130:
            assert t602006000_x11(aFlag=65700, aText=26021130)
        elif GetTalkListEntryResult() == 140:
            assert t602006000_x11(aFlag=65710, aText=26021140)
        elif GetTalkListEntryResult() == 150:
            assert t602006000_x11(aFlag=65720, aText=26021150)
        elif GetTalkListEntryResult() == 160:
            assert t602006000_x11(aFlag=65820, aText=26021160)
        elif GetTalkListEntryResult() == 170:
            assert t602006000_x11(aFlag=65800, aText=26021170)
        elif GetTalkListEntryResult() == 180:
            assert t602006000_x11(aFlag=65770, aText=26021180)
        elif GetTalkListEntryResult() == 190:
            assert t602006000_x11(aFlag=65780, aText=26021190)
        elif GetTalkListEntryResult() == 200:
            assert t602006000_x11(aFlag=65690, aText=26021200)
        elif GetTalkListEntryResult() == 210:
            assert t602006000_x11(aFlag=65740, aText=26021210)
        elif GetTalkListEntryResult() == 220:
            assert t602006000_x11(aFlag=65750, aText=26021220)
        else:
            return 0

def t602006000_x11(aFlag=0, aText=0):
    assert GetCurrentStateElapsedTime() > 0.1
    c1_110()
    while True:
        call = t602006000_x8(action2=aText+1)
        if call.Get() == 0:
            SetEventFlag(aFlag, 1)
            PlayerEquipmentQuantityChange(3, 8969, -1)
            call = t602006000_x9(action1=aText+2)
            if call.Done():
                return 0
        elif call.Done():
            return 0

