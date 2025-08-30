import json

class ReActParser:
    def parse(self, response_text: str) -> dict:
        # Trích JSON từ chuỗi text
        start = response_text.find("{")
        end = response_text.rfind("}") + 1
        json_str = response_text[start:end]
        parsed_json = json.loads(json_str)
        
        # ---- post-processing ----
        actors = list(set(parsed_json.get("actors", [])))
        
        # usecases: giữ nguyên format, không gom nhóm theo actor
        usecases_cleaned = parsed_json.get("usecases", [])
        
        # relationships: loại bỏ trùng lặp
        relationships = parsed_json.get("relationships", [])
        unique_rels = []
        seen = set()
        for rel in relationships:
            # chuyển list thành tuple để hash
            rel_hashable = {k: tuple(v) if isinstance(v, list) else v for k, v in rel.items()}
            key = tuple(sorted(rel_hashable.items()))
            if key not in seen:
                seen.add(key)
                unique_rels.append(rel)

        return {
            "actors": actors,
            "usecases": usecases_cleaned,
            "relationships": unique_rels
        }
