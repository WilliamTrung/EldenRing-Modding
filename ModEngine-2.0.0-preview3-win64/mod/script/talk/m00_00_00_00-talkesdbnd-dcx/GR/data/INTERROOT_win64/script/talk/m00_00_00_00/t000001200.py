# -*- coding: utf-8 -*-
def t000001200_1():
    """State 0,1"""
    t000001200_x0()
    Quit()

def t000001200_x0():
    """State 0"""
    if not IsClientPlayer():
        """State 1"""
        Label('L0')
        call = t000001200_x1()
        if IsClientPlayer() == 1:
            """State 2"""
            Label('L1')
            call = t000001200_x2()
            if not IsClientPlayer():
                Goto('L0')
            elif IsPlayerDead() == 1:
                pass
        elif IsPlayerDead() == 1:
            pass
    else:
        Goto('L1')
    """State 3"""
    call = t000001200_x4()
    assert not IsPlayerDead()
    Goto('L0')
    """Unused"""
    """State 4"""
    return 0

def t000001200_x1():
    """State 0"""
    while True:
        """State 1"""
        # actionbutton:6250:"Use smithing table"
        call = t000001200_x5(actionbutton1=6251, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000,
                             flag6=6000)
        if call.Done():
            """State 2"""
            call = t000001200_x3()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > 3 or IsMultiplayerInProgress() == 1:
                pass
        elif IsMultiplayerInProgress() == 1:
            pass
        """State 3"""
        assert t000001200_x6() and not IsMultiplayerInProgress()
    """Unused"""
    """State 4"""
    return 0

def t000001200_x2():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t000001200_x3():
    """State 0"""
    while True:
        """State 1"""
        Label('L0')
        ClearTalkListData()
        c1_110()
        """State 2"""
        # action:20010080:"Begin Journey <?nextLoopCount?>"
        AddTalkListDataIf(GetEventFlag(10010800) == 0 and GetEventFlag(57) == 0, 10, 20010090, -1)
        # action:20000010:"Exchange"
        AddTalkListDataIf(DoesPlayerHaveItem(3, 8990) == 1, 20, 20011030, -1)
        # action:20000010:"Exchange"
        AddTalkListDataIf(DoesPlayerHaveItem(3, 8990) == 1, 21, 20011031, -1)
        # action:20000010:"Exchange"
        AddTalkListDataIf(DoesPlayerHaveItem(3, 8990) == 1, 22, 20011032, -1)
        # action:20000010:"Exchange"
        AddTalkListDataIf(DoesPlayerHaveItem(3, 8990) == 1, 23, 20011033, -1)
        # action:20000010:"Exchange"
        AddTalkListDataIf(DoesPlayerHaveItem(3, 8990) == 1, 24, 20011034, -1)
        # action:20000010:"Exchange"
        AddTalkListDataIf(DoesPlayerHaveItem(3, 8990) == 1, 25, 20011035, -1)
        # action:20000009:"Leave"
        AddTalkListData(9, 20000009, -1)
        """State 3"""
        ShowShopMessage(1)
        assert not (CheckSpecificPersonMenuIsOpen(1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
        if GetTalkListEntryResult() == 10:
            assert t000001200_x10()
        elif GetTalkListEntryResult() == 20:
            assert t000001200_x20()
        elif GetTalkListEntryResult() == 21:
            assert t000001200_x21()
        elif GetTalkListEntryResult() == 22:
            assert t000001200_x22()
        elif GetTalkListEntryResult() == 23:
            assert t000001200_x23()
        elif GetTalkListEntryResult() == 24:
            assert t000001200_x24()
        elif GetTalkListEntryResult() == 25:
            assert t000001200_x25()
        else:
            """State 6,11"""
            return 0
    """Unused"""
    """State 7,10"""
    OpenEquipmentChangeOfPurposeShop()
    assert not (CheckSpecificPersonMenuIsOpen(7, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    Goto('L0')

def t000001200_x4():
    """State 0,2"""
    assert t000001200_x6()
    """State 1"""
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t000001200_x5(actionbutton1=6251, flag1=6001, flag2=6000, flag3=6000, flag4=6000, flag5=6000, flag6=6000):
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

def t000001200_x6():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ForceCloseGenericDialog()
    ForceCloseMenu()
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t000001200_x8(action2=_):
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

def t000001200_x9(action1=_):
    """State 0,1"""
    OpenGenericDialog(7, action1, 1, 0, 1)
    assert not CheckSpecificPersonGenericDialogIsOpen(0)
    """State 2"""
    return 0

def t000001200_x10():
    """State 0,7"""
    # action:20011080:"Begin Journey <?nextLoopCount?>?"
    call = t000001200_x11(action2=20011090)
    if call.Get() == 0:
        # action:20011081:"If you begin Journey <?nextLoopCount?>, you will not be able\nto return to the present world of Journey <?loopCount?>.\nBegin Journey <?nextLoopCount?>?"
        call = t000001200_x11(action2=20011091)
        if call.Get() == 0:
            # action:20011081:"If you begin Journey <?nextLoopCount?>, you will not be able\nto return to the present world of Journey <?loopCount?>.\nBegin Journey <?nextLoopCount?>?"
            call = t000001200_x11(action2=20011092)
            if call.Get() == 0:
                if GetEventFlag(50) == 1:
                    AwardItemLot(1000)
                    AwardItemLot(1010)
                    AwardItemLot(1020)

                    AwardItemLot(10000420)
                    AwardItemLot(11001010)
                    AwardItemLot(12020010)
                    AwardItemLot(14000500)
                    AwardItemLot(1051360070)
                    AwardItemLot(1042371010)

                    AwardItemLot(12010000)
                    AwardItemLot(12010010)
                    AwardItemLot(12020060)
                    AwardItemLot(12030000)
                    AwardItemLot(12050000)
                    AwardItemLot(1034480200)
                    AwardItemLot(1036540500)
                    AwardItemLot(1037440210)
                    AwardItemLot(1038410200)
                    AwardItemLot(1040520500)
                    AwardItemLot(1042370200)
                    AwardItemLot(1042510500)
                    AwardItemLot(1044320000)
                    AwardItemLot(1045370020)
                    AwardItemLot(1048560700)
                    AwardItemLot(1049370500)
                    AwardItemLot(1049400500)
                    AwardItemLot(1049530700)
                    AwardItemLot(1052540700)

                    AwardItemLot(10000)
                    AwardItemLot(10050)
                    AwardItemLot(101100)

                    AwardItemLot(10170)
                    AwardItemLot(30395)
                    AwardItemLot(1034430100)
                    AwardItemLot(1034500100)
                    AwardItemLot(1035470100)
                    AwardItemLot(1045330100)
                    AwardItemLot(1052410900)

                    AwardItemLot(11000130)
                    AwardItemLot(11000470)
                    AwardItemLot(16000110)
                    AwardItemLot(31180000)
                    AwardItemLot(1036510020)
                    AwardItemLot(1036520070)
                    AwardItemLot(1039510000)
                    AwardItemLot(1039540040)
                    AwardItemLot(1048380010)

                    AwardItemLot(10000770)
                    AwardItemLot(10000775)
                    AwardItemLot(11000560)
                    AwardItemLot(14000780)
                    AwardItemLot(30130100)
                    AwardItemLot(30130110)
                    AwardItemLot(30130120)
                    AwardItemLot(30130130)
                    AwardItemLot(31030020)
                    AwardItemLot(1035500400)
                    AwardItemLot(1039440100)
                    AwardItemLot(1039440110)
                    AwardItemLot(1039440120)
                    AwardItemLot(1047400010)

                    AwardItemLot(14000900)
                    AwardItemLot(30130140)
                    AwardItemLot(30130150)
                    AwardItemLot(30180040)
                    AwardItemLot(35000610)
                    AwardItemLot(1037420100)
                    AwardItemLot(1039440130)
                    AwardItemLot(1039440140)

                    AwardItemLot(102700)
                    AwardItemLot(1037460001)

                    AwardItemLot(1046380300)
                    AwardItemLot(1035490000)
                    AwardItemLot(1036420000)
                    AwardItemLot(1042390000)
                    AwardItemLot(1043340020)
                    AwardItemLot(1044530200)
                    AwardItemLot(1044530210)
                    AwardItemLot(1045370300)
                    AwardItemLot(1049370000)
                    AwardItemLot(30380)
                    AwardItemLot(30555)
                    AwardItemLot(30525)
                    AwardItemLot(30410)
                    AwardItemLot(30205)
                    AwardItemLot(30185)
                    AwardItemLot(1046380300)
                    AwardItemLot(1046380300)
                    AwardItemLot(1046380300)
                    AwardItemLot(1046380300)
                    AwardItemLot(1046380300)
                    AwardItemLot(1046380300)

                    SetEventFlag(4680, 1)
                    SetEventFlag(4699, 1)

                    GiveSpEffectToPlayer(3288)
                    GiveSpEffectToPlayer(3286)
                    GiveSpEffectToPlayer(3284)
                else:
                    AwardItemLot(1050)
                    AwardItemLot(1060)
                    AwardItemLot(1070)

                    GiveSpEffectToPlayer(3288)

                SetEventFlag(30, 1)
                Quit()
            elif call.Done():
                pass
        elif call.Done():
            pass
    elif call.Done():
        pass
    return 0

def t000001200_x11(action2=_):
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

def t000001200_x20():
    """State 0,1"""
    OpenRegularShop(50000000, 50999999)
    c1_141(5)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t000001200_x21():
    """State 0,1"""
    OpenRegularShop(51000000, 51999999)
    c1_141(5)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t000001200_x22():
    """State 0,1"""
    OpenRegularShop(52000000, 52999999)
    c1_141(5)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t000001200_x23():
    """State 0,1"""
    OpenRegularShop(53000000, 53999999)
    c1_141(5)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t000001200_x24():
    """State 0,1"""
    OpenRegularShop(54000000, 54999999)
    c1_141(5)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

def t000001200_x25():
    """State 0,1"""
    OpenRegularShop(55000000, 55999999)
    c1_141(5)
    assert not (CheckSpecificPersonMenuIsOpen(5, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0))
    """State 2"""
    return 0

