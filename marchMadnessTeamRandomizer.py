import random

def assign_regions_and_seeds():
  """
  Assigns regions (west, midwest, south, east) and seeding numbers (1-16) to 64 people.

  Returns:
    A dictionary where keys are "Person [i]" (i from 1 to 64) and values are tuples
    of (region, seed).
  """

  regions = ["west", "midwest", "south", "east"]
  seeds = list(range(1, 17))  # 1 through 16 inclusive
  assignments = {}

  # Create 4 lists, one for each region, each containing the seeds.
  region_seeds = {region: seeds[:] for region in regions}

  for i in range(1, 65):
    person_key = f"Person [{i}]"

    # Choose a random region.
    chosen_region = random.choice(regions)

    # Check if seeds are available for chosen region.
    if not region_seeds[chosen_region]:
        # if the region is out of seeds, remove it from the available regions
        regions.remove(chosen_region)
        chosen_region = random.choice(regions)

    # Choose a random seed from the chosen region's available seeds.
    chosen_seed = random.choice(region_seeds[chosen_region])

    # Remove the chosen seed from the available seeds for that region.
    region_seeds[chosen_region].remove(chosen_seed)

    assignments[person_key] = (chosen_region, chosen_seed)

  return assignments

# Example usage:
result = assign_regions_and_seeds()
for person, (region, seed) in result.items():
  print(f"{person}: Region={region}, Seed={seed}")

#check the distribution of regions and seeds.
def check_distribution(assignments):
    region_counts = {"west": 0, "midwest":0, "south":0, "east":0}
    seed_counts = {}
    for i in range(1,17):
        seed_counts[i] = 0

    for person, (region, seed) in assignments.items():
        region_counts[region]+=1
        seed_counts[seed]+=1
    print("\nRegion Counts:")
    for region, count in region_counts.items():
        print(f"{region}: {count}")

    print("\nSeed Counts:")
    for seed, count in seed_counts.items():
        print(f"{seed}: {count}")

check_distribution(result)