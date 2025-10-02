import pandas as pd
from pathlib import Path
from PopulacaoClasses import DataLoader, Analyzer, OutputWriter

IN = Path("specialist_data_engineer/projetos/Prova_aula6/População_SP.xlsx")
OUT = Path("projetos/Prova_aula6/outputs_prova_python")

df = DataLoader(IN).load()
an = Analyzer(df)
cand = an.prepare()
sexo_vals = list(df['sexo'].unique()) if 'sexo' in df.columns else []
results = []
for sx in sexo_vals:
    r = an.find_largest_age_group_by_sex(sx)
    results.append(r)

out = OutputWriter(OUT)
df_res = pd.DataFrame(results)
out.save_excel(df_res, 'parte_a_faixa_mais_populosa_por_sexo.xlsx')
out.save_json(results, 'parte_a_faixa_mais_populosa_por_sexo.json')

if results:
    chosen = results[0]
    idade = chosen.get('idade')
    sexo = chosen.get('sexo')
    most = an.municipality_with_most_for(idade, sexo)
    least = an.municipality_with_least_for(idade, sexo)
    out.save_excel(pd.DataFrame([most]), 'parte_b_municipio_mais_pessoas.xlsx')
    out.save_json([most], 'parte_b_municipio_mais_pessoas.json')
    out.save_excel(pd.DataFrame([least]), 'parte_c_municipio_menos_pessoas.xlsx')
    out.save_json([least], 'parte_c_municipio_menos_pessoas.json')

print("Processo finalizado. Saída em:", OUT)