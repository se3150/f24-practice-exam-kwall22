import pytest
from battery import Battery
from unittest.mock import Mock

todo = pytest.mark.skip(reason='todo: pending spec')

@pytest.fixture
def charged_battery():
    return Battery(100)

@pytest.fixture
def partially_charged_battery():
    b = Battery(100)
    b.mCharge = 70
    return b


def describe_Battery():
    
    def describe_init():
        
        def it_assigns_full_capacity_and_charge_attributes(charged_battery, partially_charged_battery):
            b = charged_battery
            assert b.mCapacity == 100
            assert b.mCharge == 100
        def it_assigns_partial_capacity_and_charge_attributes(charged_battery, partially_charged_battery):
            b = partially_charged_battery
            assert b.mCapacity == 100
            assert b.mCharge == 70

    def describe_getCapacity():

        def it_returns_full_and_partial_capacity(charged_battery, partially_charged_battery):
            b = charged_battery
            assert b.getCapacity() == 100
            bp = partially_charged_battery
            assert bp.getCapacity() == 100

    def describe_getCharge():
        
        def it_returns_full_and_partial_charge(charged_battery, partially_charged_battery):
            b = charged_battery
            assert b.getCharge() == 100
            bp = partially_charged_battery
            assert bp.getCharge() == 70

    def describe_recharge():
        
        def it_recharges_valid_amount(charged_battery, partially_charged_battery):
            b = partially_charged_battery
            b.recharge(10)
            assert b.getCharge() == 80
        def it_caps_recharge_amount_at_capacity(charged_battery, partially_charged_battery):
            b = partially_charged_battery
            b.recharge(40)
            assert b.getCharge() == 100
        def it_does_not_use_negative_charge_amount(charged_battery, partially_charged_battery):
            b = partially_charged_battery
            b.recharge(-20)
            assert b.getCharge() == 70
        def it_does_not_charge_if_capacity_equals_charge(charged_battery, partially_charged_battery):
            b = charged_battery
            b.recharge(5)
            assert b.getCharge() == 100
        
        def it_does_mock_stuff_for_external_monitor(mocker,partially_charged_battery):
            mock_monitor = Mock()
            mock_notify_recharge = mocker.patch.object(mock_monitor, 'notify_recharge', return_value=None)
            b = Battery(100, mock_monitor)
            b.mCharge = 60
            b.recharge(5)
            mock_notify_recharge.assert_called_once()
        
    def describe_drain():
        
        def it_drains_valid_amount(charged_battery, partially_charged_battery):
            b = charged_battery
            b.drain(5)
            assert b.getCharge() == 95
        def it_does_not_drain_on_zero_charge(charged_battery, partially_charged_battery):
            b = partially_charged_battery
            b.drain(70)
            assert b.getCharge() == 0
            b.drain(20)
            assert b.getCharge() == 0
        def it_does_not_drain_negative_amount(charged_battery, partially_charged_battery):
            b = partially_charged_battery
            b.drain(-20)
            assert b.getCharge() == 70
        
        def it_does_mock_stuff_for_external_monitor(mocker,partially_charged_battery):
            mock_monitor = Mock()
            mock_notify_drain = mocker.patch.object(mock_monitor, 'notify_drain', return_value=None)
            b = Battery(100, mock_monitor)
            b.drain(5)
            mock_notify_drain.assert_called_once()





