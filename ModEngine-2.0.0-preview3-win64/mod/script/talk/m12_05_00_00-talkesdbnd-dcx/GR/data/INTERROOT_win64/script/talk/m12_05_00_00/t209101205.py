# -*- coding: utf-8 -*-
def t209101205_1():
    """State 0"""
    while True:
        """State 2"""
        # actionbutton:6000:"Talk"
        call = t209101205_x4(flag1=9112, flag2=6001, flag3=6001, val1=5, val2=140, val3=145, val4=10,
                             val5=12, actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000, flag7=6000,
                             flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1)
        assert not GetEventFlag(12052805)
        """State 1"""
        assert GetEventFlag(12052805) == 1

def t209101205_1001():
    """State 0,2,3"""
    assert t209101205_x33()
    """State 1"""
    c1_120(1001)
    Quit()

def t209101205_1102():
    """State 0,2,3"""
    t209101205_x34()
    Quit()
    """Unused"""
    """State 1"""
    c1_120(1102)
    Quit()

def t209101205_1103():
    """State 0,2,3"""
    assert t209101205_x35()
    """State 1"""
    c1_120(1103)
    Quit()

def t209101205_x0(actionbutton1=6000, flag5=6001, flag9=6000, flag10=6000, flag11=6000, flag12=6000,
                  flag4=6000):
    """State 0"""
    while True:
        """State 1"""
        assert not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not IsCharacterDisabled()
        """State 3"""
        assert (GetEventFlag(flag5) == 1 or GetEventFlag(flag9) == 1 or GetEventFlag(flag10) == 1 or
                GetEventFlag(flag11) == 1 or GetEventFlag(flag12) == 1)
        """State 4"""
        assert not GetEventFlag(flag4)
        """State 2"""
        if GetEventFlag(flag4) == 1:
            pass
        elif (not (not GetOneLineHelpStatus() and not IsClientPlayer() and not IsPlayerDead() and not
              IsCharacterDisabled())):
            pass
        elif (not GetEventFlag(flag5) and not GetEventFlag(flag9) and not GetEventFlag(flag10) and not
              GetEventFlag(flag11) and not GetEventFlag(flag12)):
            pass
        # actionbutton:6000:"Talk"
        elif CheckActionButtonArea(actionbutton1):
            break
    """State 5"""
    return 0

def t209101205_x1():
    """State 0,1"""
    if not CheckSpecificPersonTalkHasEnded(0):
        """State 7"""
        ClearTalkProgressData()
        StopEventAnimWithoutForcingConversationEnd(0)
        """State 6"""
        ReportConversationEndToHavokBehavior()
    else:
        pass
    """State 2"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 3"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 4"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 5"""
        ForceCloseMenu()
    else:
        pass
    """State 8"""
    return 0

def t209101205_x2(val2=140, val3=145):
    """State 0,1"""
    assert GetDistanceToPlayer() < val2 and GetCurrentStateElapsedFrames() > 1
    """State 2"""
    if not f228() and not f229():
        """State 3,6"""
        call = t209101205_x18()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 5"""
            assert t209101205_x1()
    else:
        """State 4,7"""
        call = t209101205_x30()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 8"""
            assert t209101205_x1()
    """State 9"""
    return 0

def t209101205_x3():
    """State 0,1"""
    assert t209101205_x1()
    """State 2"""
    return 0

def t209101205_x4(flag1=9112, flag2=6001, flag3=6001, val1=5, val2=140, val3=145, val4=10, val5=12, actionbutton1=6000,
                  flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000,
                  z4=1000000, mode1=1, mode2=1):
    """State 0"""
    assert GetCurrentStateElapsedTime() > 1.5
    while True:
        """State 2"""
        call = t209101205_x21(flag1=flag1, flag2=flag2, flag3=flag3, val1=val1, val2=val2, val3=val3,
                              val4=val4, val5=val5, actionbutton1=actionbutton1, flag4=flag4, flag5=flag5,
                              flag6=flag6, flag7=flag7, flag8=flag8, z1=z1, z2=z2, z3=z3, z4=z4, mode1=mode1,
                              mode2=mode2)
        assert IsClientPlayer() == 1
        """State 1"""
        call = t209101205_x20()
        assert not IsClientPlayer()
    """Unused"""
    """State 3"""
    return 0

def t209101205_x5(val1=5, val2=140, val3=145, val4=10, val5=12, actionbutton1=6000, flag4=6000, flag5=6001,
                  flag6=6000, flag7=6000, flag8=6000, z1=1, z2=1000000, z3=1000000, z4=1000000, mode1=1,
                  mode2=1):
    """State 0"""
    while True:
        """State 2"""
        call = t209101205_x8(actionbutton1=actionbutton1, flag4=flag4, flag5=flag5, z2=z2, z3=z3, z4=z4)
        def WhilePaused():
            RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
            GiveSpEffectToPlayerIf(not CheckSpecificPersonTalkHasEnded(0), 9640)
        if call.Done():
            """State 4"""
            Label('L0')
            c1_138(1000000)
            call = t209101205_x12(val1=val1, z1=z1)
            def WhilePaused():
                c5_138(GetDistanceToPlayer() > 2.5, -1)
                RemoveMyAggroIf(IsAttackedBySomeone() == 1 and (DoesSelfHaveSpEffect(9626) == 1 and DoesSelfHaveSpEffect(9627) == 1))
                GiveSpEffectToPlayer(9640)
                c5_139(1 == (mode1 == 1), -1, 0)
                c5_139(1 == (mode2 == 1), 0, -1)
            def ExitPause():
                c1_138(-1)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif IsAttackedBySomeone() == 1 and not DoesSelfHaveSpEffect(9626) and not DoesSelfHaveSpEffect(9627):
            pass
        elif GetEventFlag(flag8) == 1:
            Goto('L0')
        elif GetEventFlag(flag6) == 1 and not GetEventFlag(flag7) and GetDistanceToPlayer() < val4:
            """State 5"""
            call = t209101205_x14(val5=val5)
            if call.Done():
                continue
            elif IsAttackedBySomeone() == 1:
                pass
        elif ((GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6) and not CheckSpecificPersonTalkHasEnded(0)
              and not DoesSelfHaveSpEffect(9625)):
            """State 6"""
            assert t209101205_x25() and CheckSpecificPersonTalkHasEnded(0) == 1
            continue
        elif GetEventFlag(9000) == 1:
            """State 1"""
            assert not GetEventFlag(9000)
            continue
        """State 3"""
        def ExitPause():
            RemoveMyAggro()
        assert t209101205_x10(val2=val2, val3=val3)
    """Unused"""
    """State 7"""
    return 0

def t209101205_x6(val2=140, val3=145):
    """State 0,1"""
    call = t209101205_x16(val2=val2, val3=val3)
    assert IsPlayerDead() == 1
    """State 2"""
    t209101205_x2(val2=val2, val3=val3)
    Quit()
    """Unused"""
    """State 3"""
    return 0

def t209101205_x7(flag1=9112, val2=140, val3=145):
    """State 0,8"""
    assert t209101205_x32()
    """State 1"""
    if GetEventFlag(flag1) == 1:
        """State 2"""
        pass
    else:
        """State 3"""
        if GetDistanceToPlayer() < val2:
            """State 4,6"""
            call = t209101205_x19()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t209101205_x1()
        else:
            """State 5"""
            pass
    """State 9"""
    return 0

def t209101205_x8(actionbutton1=6000, flag4=6000, flag5=6001, z2=1000000, z3=1000000, z4=1000000):
    """State 0,1"""
    call = t209101205_x9(z5=2000, val6=2000)
    if call.Get() == 1:
        """State 2"""
        assert (t209101205_x0(actionbutton1=actionbutton1, flag5=flag5, flag9=6000, flag10=6000, flag11=6000,
                flag12=6000, flag4=flag4))
    elif call.Done():
        pass
    """State 3"""
    return 0

def t209101205_x9(z5=_, val6=_):
    """State 0,1"""
    if f203(z5) == 1:
        """State 2"""
        assert GetCurrentStateElapsedFrames() > 1
        """State 4"""
        def WhilePaused():
            c1_119(z5)
        assert f202() == val6
        """State 5"""
        return 0
    else:
        """State 3,6"""
        return 1

def t209101205_x10(val2=140, val3=145):
    """State 0"""
    assert GetCurrentStateElapsedFrames() > 1
    """State 5"""
    assert t209101205_x1()
    """State 3"""
    if GetDistanceToPlayer() < val2:
        """State 1"""
        if IsPlayerAttacking() == 1:
            """State 6"""
            call = t209101205_x11()
            if call.Done():
                pass
            elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
                """State 7"""
                assert t209101205_x26()
        else:
            """State 4"""
            pass
    else:
        """State 2"""
        pass
    """State 8"""
    return 0

def t209101205_x11():
    """State 0,1"""
    assert t209101205_x9(z5=1101, val6=1101)
    """State 2"""
    return 0

def t209101205_x12(val1=5, z1=1):
    """State 0,2"""
    assert t209101205_x22()
    """State 1"""
    call = t209101205_x13()
    if call.Done():
        pass
    elif (GetDistanceToPlayer() > val1 or GetTalkInterruptReason() == 6) and not DoesSelfHaveSpEffect(9625):
        """State 3"""
        assert t209101205_x24()
    """State 4"""
    return 0

def t209101205_x13():
    """State 0,1"""
    assert t209101205_x9(z5=1000, val6=1000)
    """State 2"""
    return 0

def t209101205_x14(val5=12):
    """State 0,1"""
    call = t209101205_x15()
    if call.Done():
        pass
    elif GetDistanceToPlayer() > val5 or GetTalkInterruptReason() == 6:
        """State 2"""
        assert t209101205_x25()
    """State 3"""
    return 0

def t209101205_x15():
    """State 0,1"""
    assert t209101205_x9(z5=1100, val6=1100)
    """State 2"""
    return 0

def t209101205_x16(val2=140, val3=145):
    """State 0,5"""
    assert t209101205_x32()
    """State 2"""
    assert not GetEventFlag(3000)
    while True:
        """State 1"""
        assert GetDistanceToPlayer() < val2
        """State 3"""
        call = t209101205_x17()
        if call.Done():
            pass
        elif GetDistanceToPlayer() > val3 or GetTalkInterruptReason() == 6:
            """State 4"""
            assert t209101205_x27()
    """Unused"""
    """State 6"""
    return 0

def t209101205_x17():
    """State 0,2"""
    call = t209101205_x9(z5=1102, val6=1102)
    if call.Get() == 1:
        """State 1"""
        Quit()
    elif call.Done():
        """State 3"""
        return 0

def t209101205_x18():
    """State 0,1"""
    assert t209101205_x9(z5=1001, val6=1001)
    """State 2"""
    return 0

def t209101205_x19():
    """State 0,1"""
    assert t209101205_x9(z5=1103, val6=1103)
    """State 2"""
    return 0

def t209101205_x20():
    """State 0"""
    Quit()
    """Unused"""
    """State 1"""
    return 0

def t209101205_x21(flag1=9112, flag2=6001, flag3=6001, val1=5, val2=140, val3=145, val4=10, val5=12,
                   actionbutton1=6000, flag4=6000, flag5=6001, flag6=6000, flag7=6000, flag8=6000, z1=1,
                   z2=1000000, z3=1000000, z4=1000000, mode1=1, mode2=1):
    """State 0"""
    while True:
        """State 1"""
        RemoveMyAggro()
        call = t209101205_x5(val1=val1, val2=val2, val3=val3, val4=val4, val5=val5, actionbutton1=actionbutton1,
                             flag4=flag4, flag5=flag5, flag6=flag6, flag7=flag7, flag8=flag8, z1=z1,
                             z2=z2, z3=z3, z4=z4, mode1=mode1, mode2=mode2)
        if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
            """State 3"""
            Label('L0')
            call = t209101205_x7(flag1=flag1, val2=val2, val3=val3)
            if not CheckSelfDeath() and not GetEventFlag(flag1):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(flag2) == 1 or GetEventFlag(flag3) == 1:
            """State 2"""
            call = t209101205_x6(val2=val2, val3=val3)
            if CheckSelfDeath() == 1 or GetEventFlag(flag1) == 1:
                Goto('L0')
            elif not GetEventFlag(flag2) and not GetEventFlag(flag3):
                continue
            elif GetEventFlag(9000) == 1:
                pass
        elif GetEventFlag(9000) == 1 or IsPlayerDead() == 1:
            pass
        """State 4"""
        assert t209101205_x31() and not GetEventFlag(9000)
    """Unused"""
    """State 5"""
    return 0

def t209101205_x22():
    """State 0,1"""
    assert t209101205_x23()
    """State 2"""
    return 0

def t209101205_x23():
    """State 0,1"""
    assert t209101205_x9(z5=1104, val6=1104)
    """State 2"""
    return 0

def t209101205_x24():
    """State 0,1"""
    call = t209101205_x9(z5=1201, val6=1201)
    if call.Get() == 1:
        """State 2"""
        assert t209101205_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t209101205_x25():
    """State 0,1"""
    call = t209101205_x9(z5=1300, val6=1300)
    if call.Get() == 1:
        """State 2"""
        assert t209101205_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t209101205_x26():
    """State 0,1"""
    call = t209101205_x9(z5=1301, val6=1301)
    if call.Get() == 1:
        """State 2"""
        assert t209101205_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t209101205_x27():
    """State 0,1"""
    call = t209101205_x9(z5=1302, val6=1302)
    if call.Get() == 1:
        """State 2"""
        assert t209101205_x3()
    elif call.Done():
        pass
    """State 3"""
    return 0

def t209101205_x28(text1=_, mode3=1):
    """State 0,4"""
    assert t209101205_x29() and CheckSpecificPersonTalkHasEnded(0) == 1
    """State 1"""
    TalkToPlayer(text1, -1, -1, 1)
    """State 3"""
    if not mode3:
        pass
    else:
        """State 2"""
        ReportConversationEndToHavokBehavior()
    """State 5"""
    return 0

def t209101205_x29():
    """State 0,1"""
    ClearTalkProgressData()
    StopEventAnimWithoutForcingConversationEnd(0)
    ReportConversationEndToHavokBehavior()
    """State 2"""
    return 0

def t209101205_x30():
    """State 0,1"""
    assert t209101205_x9(z5=1002, val6=1002)
    """State 2"""
    return 0

def t209101205_x31():
    """State 0,1"""
    assert t209101205_x1()
    """State 2"""
    return 0

def t209101205_x32():
    """State 0,1"""
    if CheckSpecificPersonGenericDialogIsOpen(0) == 1:
        """State 2"""
        ForceCloseGenericDialog()
    else:
        pass
    """State 3"""
    if CheckSpecificPersonMenuIsOpen(-1, 0) == 1 and not CheckSpecificPersonGenericDialogIsOpen(0):
        """State 4"""
        ForceCloseMenu()
    else:
        pass
    """State 5"""
    return 0

def t209101205_x33():
    """State 0,2"""
    # talk:20990300:"Miquella is mine and mine alone."
    call = t209101205_x28(text1=20990300, mode3=1)
    def WhilePaused():
        c1_121(9625)
    if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
        pass
    elif GetDistanceToPlayer() > 145:
        """State 1"""
        assert t209101205_x1()
    """State 3"""
    return 0

def t209101205_x34():
    """State 0"""
    while True:
        """State 1"""
        if DoesSelfHaveSpEffect(9600) == 1 and not GetEventFlag(12052700):
            """State 2,9"""
            SetEventFlag(12052700, 1)
            """State 15"""
            # talk:20990000:"trēs"
            def WhilePaused():
                c1_121(9625)
            assert (t209101205_x28(text1=20990000, mode3=1) and (DoesSelfHaveSpEffect(9601) == 1 or CheckSpecificPersonTalkHasEnded(0)
                    == 1))
        elif DoesSelfHaveSpEffect(9601) == 1 and not GetEventFlag(12052701):
            """State 3,10"""
            SetEventFlag(12052701, 1)
            """State 16"""
            # talk:20990002:"duo"
            def WhilePaused():
                c1_121(9625)
            assert (t209101205_x28(text1=20990010, mode3=1) and (DoesSelfHaveSpEffect(9602) == 1 or CheckSpecificPersonTalkHasEnded(0)
                    == 1))
        elif DoesSelfHaveSpEffect(9602) == 1 and not GetEventFlag(12052702):
            """State 4,11"""
            SetEventFlag(12052702, 1)
            """State 17"""
            # talk:20990004:"ūnus"
            def WhilePaused():
                c1_121(9625)
            assert (t209101205_x28(text1=20990020, mode3=1) and (DoesSelfHaveSpEffect(10645) == 1 or
                    CheckSpecificPersonTalkHasEnded(0) == 1))
        elif DoesSelfHaveSpEffect(10645) == 1 and not GetEventFlag(12052703):
            """State 5,12"""
            SetEventFlag(12052703, 1)
            """State 18"""
            # talk:20990006:"nihil"
            def WhilePaused():
                c1_121(9625)
            assert (t209101205_x28(text1=20990030, mode3=1) and (DoesSelfHaveSpEffect(10646) == 1 or
                    CheckSpecificPersonTalkHasEnded(0) == 1))
        elif DoesSelfHaveSpEffect(10646) == 1 and not GetEventFlag(12052704):
            """State 6,13"""
            SetEventFlag(12052704, 1)
            """State 19"""
            # talk:20990008:"nihil"
            def WhilePaused():
                c1_121(9625)
            assert (t209101205_x28(text1=20990040, mode3=1) and (DoesSelfHaveSpEffect(10647) == 1 or
                    CheckSpecificPersonTalkHasEnded(0) == 1))
        elif DoesSelfHaveSpEffect(10647) == 1 and not GetEventFlag(12052705):
            """State 7,14"""
            SetEventFlag(12052705, 1)
            """State 20"""
            # talk:20990010:"nihil"
            def WhilePaused():
                c1_121(9625)
            assert t209101205_x28(text1=20990050, mode3=1) and CheckSpecificPersonTalkHasEnded(0) == 1
            """State 8"""
            assert not DoesSelfHaveSpEffect(10647)
    """Unused"""
    """State 21"""
    return 0

def t209101205_x35():
    """State 0,3"""
    # talk:20990500:"Ahh, I can see it, as clear as day!"
    call = t209101205_x28(text1=20990500, mode3=1)
    def WhilePaused():
        c1_121(9625)
        GiveSpEffectToPlayer(9646)
    if call.Done() and CheckSpecificPersonTalkHasEnded(0) == 1:
        pass
    elif GetDistanceToPlayer() > 145:
        """State 2"""
        assert t209101205_x1()
    """State 1"""
    SetEventFlag(12059205, 1)
    """State 4"""
    return 0

