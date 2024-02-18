# サンプル
```
curl -X POST -H "Content-Type: application/json" -d '{"format" : "small" , "cards" : ["+2 Mace", "Acererak the Archlich"]}' https://mtg-name2img-qycdsgzuoa-uc.a.run.app/image
```


# ローカルテスト
```
docker build -t name2img .;docker run --name name2img name2img pytest run_test.py;docker stop name2img;docker rm name2img
```

