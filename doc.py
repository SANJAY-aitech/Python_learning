from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

# Add Unicode font with emoji support
pdf.add_font('DejaVu', '', 'DejaVuSans.ttf', uni=True)
pdf.set_font('DejaVu', '', 12)

content = """
📊 Punjab Transport & Population Snapshot (For SIH Project)

Punjab — At a Glance
- Population (2024): ~30.99 million (~3.10 crore)
- Projected Growth: Expected to reach ~3.25 crore by 2036 (Census of India)
- Growth Rate: ~0.6–0.7% annually
- Literacy: ~75.8% overall (2011 data; male ~80.4%, female ~70.7%)

🚍 Transport & Public Mobility in Punjab
Main State Bus Operators:
- Punjab Roadways → state transport with multiple depots (Ludhiana, Jalandhar, Amritsar, etc.)
- PUNBUS → includes some GPS-enabled services
- PRTC (Pepsu Road Transport Corporation) → inter-city & rural expansion

Fleet & Modernization:
- Mix of ordinary buses (Leyland, Tata) and high-end Volvo / HVAC coaches
- Partial GPS adoption (mostly under PUNBUS)
- Government pushing e-buses under PM-eBus Sewa Scheme (Amritsar, Ludhiana, Jalandhar, Patiala prioritized)

Infrastructure & Routes:
- Major depots & bus stands across Punjab
- Example: Mohali’s Baba Banda Singh Bahadur Inter State Bus Terminus (modern, AC)
- New sub-depots in rural areas (Daula Village, Gidderbaha)

Policy Reforms:
- Free bus travel for government school students
- Expansion of routes & revival of old bus stands
- Aim: reduce dominance of private operators, strengthen govt fleet

⚠️ Gaps & Weaknesses (Opportunity Areas for Our Solution)
- Not all buses GPS-enabled → Tier-2 towns lack real-time tracking
- Poor low-bandwidth support in rural routes
- Unreliable ETA info → passengers face uncertainty
- Bus stands lack digital amenities in smaller towns
- Growing demand vs weak digital infra → free travel policy increases load but tracking lags

📍 Key Tier-2 Cities for Pilot
Jalandhar (Population ~950,000 city)
- Depot with PUNBUS GPS-enabled buses → partial real-time infra exists

Patiala (Population ~446,000 city, ~1.84M district)
- 50 new e-buses under PM-eBus scheme, govt modernization in progress

Why this matters:
- Population stats show potential impact scale
- GPS-enabled depots = we can build on existing infra (not reinventing the wheel)
- e-bus allocation = our project fits with govt modernization goals

🎯 Key Talking Points for First Slide
- Punjab: 31M people, growing cities, rising transport demand
- Tier-2 towns: commuters + students face unpredictable bus services
- Current gap: only partial GPS tracking, poor real-time info
- Your solution: low-bandwidth friendly, real-time tracking system for small cities
- Pilot cities: Jalandhar & Patiala (already have infra + future e-bus plans)

✅ Evaluator’s Angle: Highlighting population, gaps, and city-level infra shows you’re solving a real, validated problem — not an abstract idea.
"""

for line in content.split("\n"):
    pdf.multi_cell(0, 10, line)

file_path = "Punjab_Transport_Project_Summary.pdf"
pdf.output(file_path)
