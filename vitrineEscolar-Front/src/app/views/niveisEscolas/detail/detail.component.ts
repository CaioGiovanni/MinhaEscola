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
  avaliacoes:any=[];
  input: any;
  data = new Date();

  constructor(private service:SharedService, private route: ActivatedRoute) { 
    this.route.params.subscribe(params => this.selectedSchool = params['id']);
  }

  ngOnInit(): void {
    this.input = {
      ano: this.pegaData(),
      avaliador: -1,
      escolaAvaliada: -1,
      segurancaEscolar: 0,
      estruturaEscolar: 0,
      alimentacaoEscolar: 0,
      qualidadeEscolar: 0,
      comentario: '',
      rankingDaAvaliacao: 1
    };
    this.refreshDepList();
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
      this.selectedSchool = this.getSchool(this.selectedSchool);
      this.service.getEscola(this.selectedSchool.pk).subscribe(data2=>{
        this.selectedSchool=data2;
        this.avaliacoes = this.selectedSchool.avaliacoes[0];
        this.selectedSchool = this.selectedSchool.escola;
      });
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
          this.input.avaliador = data2.usuario.usuario.pk;
          this.input.escolaAvaliada = this.selectedSchool.pk;

          this.service.postAvaliacao(this.input).subscribe(
            response => {
              console.log(response);
              alert(response);
            },
            error => {
              console.log('error', error);
              alert("Não foi possível realizar a avaliação.");
            }
          )
        });
      });
    }
  }

  pegaData() {
    var data = new Date();
    var dia = data.getDate();
    var mes = data.getMonth() + 1;
    var ano = data.getFullYear();
    return [dia, mes, ano].join('/');
  }
}
