
class Perangkat:
    def __init__(self, nama, daya, kepentingan):
        self.nama = nama
        self.daya = daya          
        self.kepentingan = kepentingan  

def tampilkan_data_awal(daftar_perangkat):
    print("\n[ DATA PERANGKAT TERSEDIA - SEBELUM TERPILIH ]")
    print("-" * 65)
    print(f"{'No':<4} | {'Nama Perangkat':<20} | {'Daya (wi)':<12} | {'Profit (pi)':<10}")
    print("-" * 65)
    for i, p in enumerate(daftar_perangkat, 1):
        print(f"{i:<4} | {p.nama:<20} | {p.daya:>3} Watt    | {p.kepentingan:>8}")
    print("-" * 65)

def solve_kos_backtracking():
    
    perangkat = [
        Perangkat("Laptop Gaming", 200, 95),
        Perangkat("Rice Cooker", 350, 90),
        Perangkat("AC Portable", 400, 85),
        Perangkat("Kipas Angin", 50, 60),
        Perangkat("Lampu Belajar LED", 10, 40),
        Perangkat("Dispenser (Hot)", 300, 50),
        Perangkat("Setrika Listrik", 300, 45),
        Perangkat("Speaker Monitor", 40, 30),
        Perangkat("Charger HP", 25, 70),
        Perangkat("Teko Listrik", 450, 20)
    ]

    kapasitas_m = 900 
    n = len(perangkat)
    
    
    tampilkan_data_awal(perangkat)
    
    max_profit = 0
    best_combination = []


    def backtrack(index, current_weight, current_profit, selected_indices):
        nonlocal max_profit, best_combination

       
        if index == n:
            if current_profit > max_profit:
                max_profit = current_profit
                best_combination = list(selected_indices)
            return

        
        if current_weight + perangkat[index].daya <= kapasitas_m:
            selected_indices.append(index)
            backtrack(index + 1, 
                      current_weight + perangkat[index].daya, 
                      current_profit + perangkat[index].kepentingan, 
                      selected_indices)
            selected_indices.pop() # Backtrack

        backtrack(index + 1, current_weight, current_profit, selected_indices)

    backtrack(0, 0, 0, [])

    print("\n[ HASIL OPTIMASI ALGORITMA - SESUDAH TERPILIH ]")
    print("-" * 65)
    total_w = 0
    for idx in best_combination:
        p = perangkat[idx]
        total_w += p.daya
        print(f"✅ AKTIF: {p.nama:<20} | {p.daya:>3} Watt | Nilai: {p.kepentingan}")

    print("-" * 65)
    print(f"TOTAL NILAI KEPENTINGAN (Max Z) : {max_profit}") 
    print(f"TOTAL DAYA TERPAKAI             : {total_w} / {kapasitas_m} Watt") 
    print(f"SISA DAYA                       : {kapasitas_m - total_w} Watt")
    print("-" * 65)

if __name__ == "__main__":
    solve_kos_backtracking()