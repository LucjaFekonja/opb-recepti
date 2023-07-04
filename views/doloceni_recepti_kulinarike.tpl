% rebase('osnova.tpl')

<table class="navigacija">
    <tr>
        <th class="nav-stolpec-1">
            <form action="{{url('moji_recepti')}}" method="GET">
                <button class="gumb-moji-recepti" type="submit">Moji recepti</button>
            </form>
        </th>
        <th class="nav-stolpec-1">
            <form action="{{url('vsi_recepti_prijava')}}" method="GET">
                <button class="gumb-moji-recepti" type="submit">Vsi recepti</button>
            </form>
        </th>
        <th class="nav-stolpec-1"></th>
        <th class="nav-stolpec-mid">
            <div class="dropdown">
                Kategorije
                <div class="dropdown-content">
                    % for kategorija in kategorije:
                        <a href="{{url('doloceni_recepti_kat', kategorija=kategorija)}}">{{kategorija}}</a><br>
                    % end
                </div>
            </div>
        </th>
        <th class="nav-stolpec-mid">
            <div class="dropdown">
                Kulinarike
                <div class="dropdown-content">
                    % for kulinarika in kulinarike:
                        <a href="{{url('doloceni_recepti_kul', kulinarika=kulinarika)}}">{{kulinarika}}</a><br>
                    % end
                </div>
            </div>
        </th>
        <th class="nav-stolpec-mid">
            <div class="dropdown">
                Oznake
                <div class="dropdown-content" style="height: 500px;">
                    % for oznaka in oznake:
                        <a href="{{url('doloceni_recepti_oz', oznaka=oznaka)}}">{{oznaka}}</a><br>
                    % end
                </div>
            </div>
        </th>
        <th class="nav-stolpec-1"></th>
        <th class="nav-stolpec-1"></th>
        <th class="nav-stolpec-1">
            <div class="dropdown" style="text-align: center;">
                ° ° °
                <div class="dropdown-content">
                    <div class="button">
                        <a class="button" href="{{url('prijava_get')}}" method="GET">Prijava</a><br>
                    </div>
                    <div class="button">
                        <a class="button" href="{{url('odjava')}}" method="GET">Odjava</a><br>
                    </div>
                </div>
            </div>
        </th>
    </tr>
</table>


<div class="center" style="color: darkred;top: 100px;">
    <h1>{{izb_kulinarika}}</h1>
</div>


<table class="tabela" id="recepti">
    <tr class="prva-vrstica">
        <td>
            <form action="{{url('uredi_kulinarika', param='ime', kulinarika=izb_kulinarika)}}" method="get">
                <a href="#" onclick="this.parentElement.submit()" class="th-link" style="color: black;">ime recepta ⏷</a>
            </form>
        </td>
        <td>
            <form action="{{url('uredi_kulinarika', param='st_porcij', kulinarika=izb_kulinarika)}}" method="get">
                <a href="#" onclick="this.parentElement.submit()" class="th-link" style="color: black;">število porcij ⏷</a>
            </form>
        </td>
        <td>
            <form action="{{url('uredi_kulinarika', param='cas_priprave', kulinarika=izb_kulinarika)}}" method="get">
                <a href="#" onclick="this.parentElement.submit()" class="th-link" style="color: black;">čas priprave ⏷</a>
            </form>
        </td>
        <td>
            <form action="{{url('uredi_kulinarika', param='cas_kuhanja', kulinarika=izb_kulinarika)}}" method="get">
                <a href="#" onclick="this.parentElement.submit()" class="th-link" style="color: black;">čas kuhanja ⏷</a>
            </form>
        </td>
    </tr>
     % for recept in recepti:
        <tr class="vrstica">
            <td>
                <form action="{{url('pojdi_na_recept', id=recept.id)}}" method="POST">
                    <button class="gumb" style="text-align: left;" type="submit">{{recept.ime}}</button> 
                </form>
            </td>
            <td>{{recept.st_porcij}}</td>
            <td>{{recept.cas_priprave}}</td>
            <td>{{recept.cas_kuhanja}}</td>
        </tr>
    %end
</table>
