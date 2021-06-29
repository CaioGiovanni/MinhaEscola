import { Component, OnInit } from '@angular/core';
import { observable, Observable } from 'rxjs';
import { SharedService} from 'src/app/shared.service';
import { ActivatedRoute, Router } from '@angular/router';

@Component({
  selector: 'app-cadastro',
  templateUrl: './cadastro.component.html',
  styleUrls: ['./cadastro.component.css']
})
export class CadastroComponent implements OnInit {

  EscolaList:any=[];
  input: any;

  constructor(private service:SharedService, private route: ActivatedRoute, private router:Router) { }

  ngOnInit(): void {
    this.input = {
      usuario: '',
      nome: '',
      sobrenome: '',
      email: '',
      senha: '',
      confirmarSenha: '',
      dataNascimento: '',
      escolaAtual: '',
      cep: '',
      telefone: '',
    };
    this.refreshDepList();
  }

  register(): void {
    this.service.registerUser(this.input).subscribe(
      response => {
        console.log(response);
        alert(response.mensagem);
        // alert('Usuário ' + this.input.usuario + ' cadastrado.');
      },
      error => {
        console.log('error', error);
      }
    )
  }

  refreshDepList() {
    this.service.getEscolaList().subscribe(data=>{
      this.EscolaList=data;
    });
  }
}
