from src.entries.bos_entry import detect_bos
from src.entries.liquidity_entry import detect_liquidity_sweep
from src.entries.fvg_entry import detect_fvg

def run_scanner():
    print("🔎 Scanner is running...")
    bos = detect_bos()
    liquidity = detect_liquidity_sweep()
    fvg = detect_fvg()
    setups_found = sum([bos['found'], liquidity['found'], fvg['found']])
    return {'status': 'ok', 'setups_found': setups_found}
