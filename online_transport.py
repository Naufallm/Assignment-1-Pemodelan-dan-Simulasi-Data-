import simpy
import random

class DigitalService:
    def __init__(self, env, num_agents, service_time_range=(1, 3)):
        self.env = env
        self.agent_pool = simpy.Resource(env, num_agents)
        self.wait_times = []
        self.service_time_range = service_time_range

    def customer(self, name):
        arrival_time = self.env.now
        print(f"{name} arrived at {arrival_time:.2f} minutes.")

        with self.agent_pool.request() as request:
            yield request  # Menunggu agen tersedia
            
            wait_time = self.env.now - arrival_time
            self.wait_times.append(wait_time)
            print(f"{name} started service after waiting {wait_time:.2f} minutes.")

            # Simulasi waktu layanan 
            service_time = random.uniform(*self.service_time_range)
            yield self.env.timeout(service_time)

    def customer_arrival(self, arrival_rate):
        customer_id = 1
        while True:
            yield self.env.timeout(random.expovariate(1.0 / arrival_rate))  
            self.env.process(self.customer(f"Customer {customer_id}"))
            customer_id += 1

# Eksekusi Simulasi
def run_simulation(num_agents=1, arrival_rate=5, sim_time=10):
    env = simpy.Environment()
    service = DigitalService(env, num_agents, service_time_range=(2, 5))  
    env.process(service.customer_arrival(arrival_rate))
    env.run(until=sim_time)

    # Analisis hasil
    avg_wait = sum(service.wait_times) / len(service.wait_times) if service.wait_times else 0
    max_wait = max(service.wait_times, default=0)
    min_wait = min(service.wait_times, default=0)

    print("\n=== Simulation Summary ===")
    print(f"Average Wait Time: {avg_wait:.2f} minutes")
    print(f"Max Wait Time: {max_wait:.2f} minutes")
    print(f"Min Wait Time: {min_wait:.2f} minutes")

# Jalankan simulasi
run_simulation(num_agents=1, arrival_rate=5, sim_time=10)
