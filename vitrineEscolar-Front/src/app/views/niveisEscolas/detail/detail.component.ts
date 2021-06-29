import { Component, OnInit } from '@angular/core';
import { SharedService} from 'src/app/shared.service';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-detail',
  templateUrl: './detail.component.html',
  styleUrls: ['./detail.component.css']
})
export class DetailComponent implements OnInit {

  EscolaList:any=[];
  selectedSchool:any;
  input: any;

  constructor(private service:SharedService, private route: ActivatedRoute) { 
    this.route.params.subscribe(params => this.selectedSchool = params['id']);
  }

  ngOnInit(): void {
    this.input = {
      seguranca: 0,
      estrutura: 0,
      Merenda: 0,
      Metodologia: 0,
      comentario: ''
    };
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
      this.selectedSchool = this.getSchool(this.selectedSchool);
      console.log(this.selectedSchool.avaliacoes)
      /*this.service.getEscola(this.selectedSchool).subscribe(data=>{
        this.selectedSchool=data;
        console.log(data)
      });*/
    });
  }

  getSchool(pk: any) {
    return this.EscolaList?.results.find((escola: any) => escola.pk === parseInt(pk));
  }

  avalia() {
    if (localStorage.getItem("Access key") === null) {
      alert('Nenhum usuário encontrado. Por favor, realize o login.')
    }
    else {
      this.service.refreshKey().subscribe(data=>{
        localStorage.setItem("Access key", data.access);
        this.service.getUsuario().subscribe(data2=>{
          console.log(data2.usuario.usuario.pk);
          console.log(this.input)
          // Falta adicionar escola avaliada e o ano
        });
      });
    }
  }
}
