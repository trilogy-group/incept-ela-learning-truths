import json, time, urllib.request, concurrent.futures as cf, sys, os
B = "http://127.0.0.1:4310"
def post(p, body, t=600):
    return json.load(urllib.request.urlopen(urllib.request.Request(B + p, data=json.dumps(body).encode(), method="POST"), timeout=t))
samples = json.load(urllib.request.urlopen(B + "/api/samples"))["samples"]
texts = {"ozymandias": next(s["text"] for s in samples if s["title"].startswith("Ozymandias")),
         "gettysburg": open(os.path.join(os.path.dirname(__file__), "gettysburg.txt")).read()}
mechs = [m["id"] for m in json.load(urllib.request.urlopen(B + "/api/mechanics"))["mechanics"]]
out = {"questions": {}, "blocks": []}
for k, t in texts.items():
    q = post("/api/suggest-question", {"text": t}, 300)
    out["questions"][k] = q.get("question")
def make(job):
    k, m = job; t0 = time.time()
    try:
        b = post("/api/block", {"text": texts[k], "question": out["questions"][k], "mechanic": m, "n": 1})
        return {"text": k, "mechanic": m, "status": b["status"], "key": b["key"], "seconds": round(time.time() - t0, 1)}
    except Exception as e:
        return {"text": k, "mechanic": m, "status": "error", "error": str(e)[:200], "seconds": round(time.time() - t0, 1)}
with cf.ThreadPoolExecutor(8) as ex:
    out["blocks"] = list(ex.map(make, [(k, m) for k in texts for m in mechs]))
json.dump(out, open(os.path.join(os.path.dirname(__file__), "result.json"), "w"), indent=1)
print("done", sum(1 for b in out["blocks"] if b["status"] == "ready"), "/", len(out["blocks"]), "ready")
