# Analyse du code - Tri à bulles

## ✅ Points positifs
- La logique du tri à bulles est **correcte**
- Le code est **lisible** et bien structuré
- L'exemple d'utilisation fonctionne bien

## ⚠️ Problèmes et améliorations

### 1. **Modification de la liste originale (effet de bord)**
```python
# ❌ PROBLÈME
ma_liste = [64, 34, 25, 12, 22, 11, 90]
ma_liste_triee = tri_bulle(ma_liste)
print(ma_liste)  # ❌ Ma_liste est aussi modifiée !
```

**Solution :** Copier la liste
```python
def tri_bulle(liste):
    n = len(liste.copy())  # ✅ Ou utiliser liste[:] ou list(liste)
    liste = liste.copy()
    # ...
```

### 2. **Optimisation possible - Flag d'amélioration**
```python
def tri_bulle(liste):
    n = len(liste)
    liste = liste.copy()
    for i in range(n):
        echange = False  # ✅ Nouveau
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                echange = True
        if not echange:  # ✅ Si pas d'échange, c'est trié !
            break
    return liste
```

### 3. **Pas de gestion des erreurs**
```python
def tri_bulle(liste):
    if not isinstance(liste, list):
        raise TypeError("L'argument doit être une liste")
    if not liste:  # ✅ Gérer liste vide
        return []
    
    n = len(liste)
    liste = liste.copy()
    for i in range(n):
        echange = False
        for j in range(0, n-i-1):
            if liste[j] > liste[j+1]:
                liste[j], liste[j+1] = liste[j+1], liste[j]
                echange = True
        if not echange:
            break
    return liste
```

### 4. **Pas de docstring**
```python
def tri_bulle(liste):
    """
    Trie une liste en utilisant l'algorithme du tri à bulles.
    
    Args:
        liste (list): La liste à trier
        
    Returns:
        list: Une nouvelle liste triée
        
    Exemple:
        >>> tri_bulle([3, 1, 2])
        [1, 2, 3]
    """
```

---

## 📋 Code amélioré complet

```python
#!/usr/bin/env python3

def tri_bulle(liste):
    """
    Trie une liste en utilisant l'algorithme du tri à bulles.
    
    Args:
        liste (list): La liste à trier
        
    Returns:
        list: Une nouvelle liste triée
        
    Raises:
        TypeError: Si l'argument n'est pas une liste
    """
    if not isinstance(liste, list):
        raise TypeError("L'argument doit être une liste")
    
    if not liste:
        return []
    
    n = len(liste)
    resultat = liste.copy()  # ✅ Copie pour ne pas modifier l'original
    
    for i in range(n):
        echange = False
        for j in range(0, n-i-1):
            if resultat[j] > resultat[j+1]:
                resultat[j], resultat[j+1] = resultat[j+1], resultat[j]
                echange = True
        
        if not echange:  # ✅ Optimisation : arrêter si déjà trié
            break
    
    return resultat


# Tests
if __name__ == "__main__":
    ma_